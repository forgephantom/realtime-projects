#!/usr/bin/env python3
"""Mediator (Chatroom): Chat Server.

A mediator centralizes communication: chatroom members send messages to the mediator, which routes to recipients, instead of everyone referencing everyone. It turns N-to-N wiring into N-to-1. Private messages, moderation, and presence all live in the mediator.

Demo dataset idea: Routes seeded chat traffic through the mediator, verifying delivery rules and moderation..
"""

import argparse
import random
import socket
import threading
import time

SLUG = "mediator-chatroom-chat_server-beginner"
PARAMS = {'members': 'participant count', 'routing': 'broadcast vs direct vs rooms', 'moderation': 'mute/ban capabilities'}
HOST = "127.0.0.1"  # loopback only: this server never binds a public interface


class ChatServer:
    """A tiny TCP chat relay bound to 127.0.0.1 on an ephemeral port.

    Each client gets a reader thread; every newline-terminated line a client
    sends is broadcast to all other connected clients.
    """

    def __init__(self, host: str = HOST):
        self.host = host
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.bind((host, 0))  # ephemeral port chosen by the OS
        self._sock.listen(8)
        self._clients = []
        self._lock = threading.Lock()
        self._running = False
        self._accept_thread = None

    @property
    def port(self) -> int:
        """The ephemeral port the OS assigned at bind time."""
        return self._sock.getsockname()[1]

    def start(self) -> None:
        """Begin accepting clients in a background thread."""
        self._running = True
        self._accept_thread = threading.Thread(target=self._accept_loop, daemon=True)
        self._accept_thread.start()

    def _accept_loop(self) -> None:
        self._sock.settimeout(0.2)
        while self._running:
            try:
                conn, _ = self._sock.accept()
            except socket.timeout:
                continue
            except OSError:
                return
            conn.settimeout(0.2)
            with self._lock:
                self._clients.append(conn)
            threading.Thread(target=self._relay, args=(conn,), daemon=True).start()

    def _relay(self, conn) -> None:
        buf = b""
        while self._running:
            try:
                chunk = conn.recv(4096)
            except socket.timeout:
                continue
            except OSError:
                break
            if not chunk:
                break
            buf += chunk
            while b"\n" in buf:
                line, buf = buf.split(b"\n", 1)
                self.broadcast(line + b"\n", exclude=conn)
        with self._lock:
            if conn in self._clients:
                self._clients.remove(conn)
        try:
            conn.close()
        except OSError:
            pass

    def broadcast(self, data: bytes, exclude=None) -> None:
        """Send raw bytes to every client except exclude."""
        with self._lock:
            targets = [c for c in self._clients if c is not exclude]
        for target in targets:
            try:
                target.sendall(data)
            except OSError:
                pass

    def client_count(self) -> int:
        """Number of currently connected clients."""
        with self._lock:
            return len(self._clients)

    def shutdown(self) -> None:
        """Stop accepting, disconnect clients, and release the socket."""
        self._running = False
        with self._lock:
            clients = list(self._clients)
        for conn in clients:
            try:
                conn.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass
            try:
                conn.close()
            except OSError:
                pass
        try:
            self._sock.close()
        except OSError:
            pass
        if self._accept_thread is not None:
            self._accept_thread.join(timeout=2.0)


class ChatClient:
    """A blocking-line chat client with a background reader thread."""

    def __init__(self, name: str, host: str, port: int):
        self.name = name
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect((host, port))
        self._sock.settimeout(0.2)
        self._inbox = []
        self._lock = threading.Lock()
        self._running = True
        self._reader = threading.Thread(target=self._read_loop, daemon=True)
        self._reader.start()

    def send(self, text: str) -> None:
        """Send one chat line, prefixed with this client's name."""
        self._sock.sendall(("%s: %s\n" % (self.name, text)).encode())

    def _read_loop(self) -> None:
        buf = b""
        while self._running:
            try:
                chunk = self._sock.recv(4096)
            except socket.timeout:
                continue
            except OSError:
                return
            if not chunk:
                return
            buf += chunk
            while b"\n" in buf:
                line, buf = buf.split(b"\n", 1)
                with self._lock:
                    self._inbox.append(line.decode(errors="replace"))

    def received(self) -> list:
        """A snapshot of every line received so far."""
        with self._lock:
            return list(self._inbox)

    def close(self) -> None:
        """Stop the reader and release the socket."""
        self._running = False
        try:
            self._sock.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        try:
            self._sock.close()
        except OSError:
            pass
        self._reader.join(timeout=2.0)


def run_self_test(messages_per_client: int) -> int:
    """Spin up a server plus two scripted clients, exchange messages, verify."""
    server = ChatServer()
    server.start()
    alice = ChatClient("alice", HOST, server.port)
    bob = ChatClient("bob", HOST, server.port)
    time.sleep(0.2)  # let both clients register with the server

    alice_lines = ["hello from the Mediator (Chatroom) demo (%d/%d)" % (i + 1, messages_per_client)
                   for i in range(messages_per_client)]
    bob_lines = ["ack %d: A mediator centralizes communication: chatroom members send messages to the mediator, which routes to recipients, instead of everyone referencing everyone. It turns N-to-N wiring into N-to-1. Private messages, moderation, and presence all live in the mediator." % (i + 1)
                 for i in range(messages_per_client)]
    for a_line, b_line in zip(alice_lines, bob_lines):
        alice.send(a_line)
        time.sleep(0.05)
        bob.send(b_line)
        time.sleep(0.05)
    time.sleep(0.5)  # let the last broadcasts land

    alice_got = alice.received()
    bob_got = bob.received()
    expected_for_alice = ["bob: " + line for line in bob_lines]
    expected_for_bob = ["alice: " + line for line in alice_lines]
    ok = alice_got == expected_for_alice and bob_got == expected_for_bob

    print("Mediator (Chatroom): Chat Server  (topic: Mediator (Chatroom))")
    print("Self-test: server on %s:%d, 2 clients x %d messages" % (
        HOST, server.port, messages_per_client))
    print("\nalice received (%d):" % len(alice_got))
    for line in alice_got:
        print("  " + line)
    print("\nbob received (%d):" % len(bob_got))
    for line in bob_got:
        print("  " + line)
    print("\nRelay check: %s" % ("PASS - every message reached the other client"
                                if ok else "FAIL - transcript mismatch"))

    alice.close()
    bob.close()
    server.shutdown()
    return 0 if ok else 1


def run_serve() -> int:
    """Run the server persistently until Ctrl-C."""
    server = ChatServer()
    server.start()
    print("Mediator (Chatroom): Chat Server serving on %s:%d (Ctrl-C to stop)" % (HOST, server.port))
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nShutting down.")
    server.shutdown()
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Mediator (Chatroom): Chat Server: A mediator centralizes communication: chatroom members send messages to the mediator, which routes to recipients, instead of everyone referencing everyone. It turns N-to-N wiring into N-to-1. Private messages, moderation, and presence all live in the mediator."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed (default: 42).")
    parser.add_argument("--serve", action="store_true",
                        help="Run the server persistently instead of the self-test.")
    parser.add_argument("--messages", type=int, default=None,
                        help="Messages per client in the self-test (see the topic params).")
    return parser


def main(argv=None) -> int:
    """Entry point: self-test by default, persistent server with --serve."""
    args = build_parser().parse_args(argv)
    random.seed(args.seed)
    if args.serve:
        return run_serve()
    messages = args.messages or int(PARAMS.get("messages_per_client", 3))
    return run_self_test(messages)


if __name__ == "__main__":
    raise SystemExit(main())
