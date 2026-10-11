#!/usr/bin/env python3
"""MCP Elicitation Flow Simulator: Chatbot.

Elicitation lets a server request structured input from the user through the client: the server sends a schema, the client renders a form, and the user's answers come back validated. It keeps sensitive input handling on the client side. The simulator runs seeded elicitation flows with validation retries.

Demo dataset idea: Simulates seeded elicitation requests with schemas and user answer patterns, measuring validation pass rates and retry counts..
"""

import argparse
import random

SLUG = "mcp-elicitation-flow-chatbot-intermediate"
PARAMS = {'fields': 'form fields per request', 'num_requests': 'elicitation requests', 'retry_limit': 'validation retries allowed'}


def build_intents() -> list:
    """The bot's intent table: name, keyword triggers, and canned responses."""
    topic = "MCP Elicitation Flow Simulator"
    concept = "Elicitation lets a server request structured input from the user through the client: the server sends a schema, the client renders a form, and the user's answers come back validated. It keeps sensitive input handling on the client side. The simulator runs seeded elicitation flows with validation retries."
    return [
        {"name": "greeting",
         "keywords": ["hello", "hi", "hey", "good morning", "good afternoon"],
         "responses": ["Hello! I am %s, a demo %s." % (SLUG, topic),
                       "Hi there! Ask me what this %s is about." % topic]},
        {"name": "concept",
         "keywords": ["what", "about", "topic", "concept", "idea", "project", "demo"],
         "responses": ["%s: %s" % (topic, concept)]},
        {"name": "run",
         "keywords": ["run", "start", "execute", "launch", "how do"],
         "responses": ["Run `python3 src/main.py` with no arguments for the scripted "
                       "demo, or `python3 src/main.py --chat` to talk to me."]},
        {"name": "help",
         "keywords": ["help", "commands", "options", "usage"],
         "responses": ["I understand greetings, questions about the %s, how to run "
                       "the demo, and goodbyes. Try 'what is this about?'." % topic]},
        {"name": "bye",
         "keywords": ["bye", "goodbye", "quit", "exit", "see you"],
         "responses": ["Goodbye! Thanks for trying the %s demo." % topic,
                       "See you next time!"]},
        {"name": "fallback",
         "keywords": [],
         "responses": ["I did not catch that. I know about %s - ask me "
                       "'what is it about?' or type 'help'." % topic]},
    ]


class Chatbot:
    """A tiny rule-based chatbot: keyword scoring picks the intent."""

    def __init__(self, name: str, intents: list, seed: int = 42):
        self.name = name
        self.intents = intents
        self.turns = 0
        self._rng = random.Random(seed)

    def match_intent(self, text: str) -> dict:
        """Score each intent by keyword hits; ties go to the first intent."""
        lowered = text.lower()
        best, best_score = self.intents[-1], 0  # default: fallback
        for intent in self.intents:
            score = sum(1 for kw in intent["keywords"] if kw in lowered)
            if score > best_score:
                best, best_score = intent, score
        return best

    def respond(self, text: str) -> tuple:
        """Return (intent_name, response) for one user message."""
        self.turns += 1
        intent = self.match_intent(text)
        return (intent["name"], self._rng.choice(intent["responses"]))


def run_demo(seed: int) -> int:
    """Play a scripted conversation and print the transcript with intents."""
    bot = Chatbot(SLUG, build_intents(), seed=seed)
    script = ["hello",
              "what is this about?",
              "how do I run the demo?",
              "help",
              "ok thanks, bye"]
    print("MCP Elicitation Flow Simulator: Chatbot  (topic: MCP Elicitation Flow Simulator, seed=%d)" % seed)
    print("Scripted conversation:\n")
    for line in script:
        intent_name, reply = bot.respond(line)
        print("you: %s" % line)
        print("%s [intent=%s]: %s\n" % (bot.name, intent_name, reply))
    print("Conversation over: %d turns." % bot.turns)
    return 0


def run_chat(seed: int) -> int:
    """Interactive chat loop; say 'bye' to quit."""
    bot = Chatbot(SLUG, build_intents(), seed=seed)
    print("MCP Elicitation Flow Simulator: Chatbot - chatting as %s. Say 'bye' to quit.\n" % bot.name)
    while True:
        try:
            line = input("you: ")
        except EOFError:
            print()
            break
        if not line.strip():
            continue
        intent_name, reply = bot.respond(line)
        print("%s: %s" % (bot.name, reply))
        if intent_name == "bye":
            break
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="MCP Elicitation Flow Simulator: Chatbot: Elicitation lets a server request structured input from the user through the client: the server sends a schema, the client renders a form, and the user's answers come back validated. It keeps sensitive input handling on the client side. The simulator runs seeded elicitation flows with validation retries."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--chat", action="store_true",
                        help="Chat interactively via input() instead of the scripted demo.")
    parser.add_argument("--name", type=str, default=SLUG,
                        help="Bot display name (default: mcp-elicitation-flow-chatbot-intermediate).")
    return parser


def main(argv=None) -> int:
    """Entry point: scripted demo by default, --chat for interactive mode."""
    args = build_parser().parse_args(argv)
    random.seed(args.seed)
    if args.chat:
        return run_chat(args.seed)
    return run_demo(args.seed)


if __name__ == "__main__":
    raise SystemExit(main())
