#!/usr/bin/env python3
"""Cap-and-Trade Market Simulator: Terminal Game.

Cap-and-trade sets a total emissions cap and lets firms buy and sell allowances, so the allowance price emerges where supply meets demand. The simulator runs trading rounds among firms with different abatement costs to find the clearing price.

Demo dataset idea: Seeded RNG assigns firms random abatement cost curves and the simulator clears the allowance market..
"""

import argparse
import random

SLUG = "cap-and-trade-simulator-terminal_game-beginner"
PARAMS = {'cap_tons': 'total cap in tons', 'firms': 'number of participating firms', 'rounds': 'trading rounds'}

EMPTY = " "
WIN_LINES = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
             (0, 3, 6), (1, 4, 7), (2, 5, 8),
             (0, 4, 8), (2, 4, 6))
# Center-first move order keeps the AI's play deterministic and sensible.
MOVE_ORDER = (4, 0, 2, 6, 8, 1, 3, 5, 7)


def new_board() -> list:
    """A fresh 3x3 board as a list of 9 cells."""
    return [EMPTY] * 9


def available_moves(board: list) -> list:
    """Empty cell indexes, in the fixed MOVE_ORDER."""
    return [i for i in MOVE_ORDER if board[i] == EMPTY]


def winner(board: list):
    """'X', 'O', 'draw', or None when the game is still going."""
    for a, b, c in WIN_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    if EMPTY not in board:
        return "draw"
    return None


def minimax(board: list, player: str) -> tuple:
    """Full-depth minimax: return (score, best_move); X maximizes, O minimizes."""
    result = winner(board)
    if result == "X":
        return (1, None)
    if result == "O":
        return (-1, None)
    if result == "draw":
        return (0, None)
    if player == "X":
        best_score, best_move = -2, None
        for move in available_moves(board):
            board[move] = "X"
            score, _ = minimax(board, "O")
            board[move] = EMPTY
            if score > best_score:
                best_score, best_move = score, move
        return (best_score, best_move)
    best_score, best_move = 2, None
    for move in available_moves(board):
        board[move] = "O"
        score, _ = minimax(board, "X")
        board[move] = EMPTY
        if score < best_score:
            best_score, best_move = score, move
    return (best_score, best_move)


def render(board: list) -> str:
    """The board as a printable 3x3 grid."""
    rows = []
    for r in range(3):
        rows.append(" %s | %s | %s " % tuple(board[r * 3:(r + 1) * 3]))
    return "\n---+---+---\n".join(rows)


def play_game(x_move, o_move) -> tuple:
    """Play one game; move functions take a board copy and return a cell index.
    Returns (result, moves) where result is 'X', 'O', or 'draw'."""
    board = new_board()
    moves = []
    player, fn = "X", x_move
    while winner(board) is None:
        move = fn(list(board))
        if move not in available_moves(board):
            raise ValueError("illegal move %r by %s" % (move, player))
        board[move] = player
        moves.append((player, move))
        player, fn = ("O", o_move) if player == "X" else ("X", x_move)
    return (winner(board), moves)


def ai_player(board: list) -> int:
    """Minimax move for whoever is to move on this board."""
    player = "X" if board.count("X") <= board.count("O") else "O"
    _, move = minimax(board, player)
    return move


def make_random_player(rng: random.Random):
    """A player function that picks uniformly at random from legal moves."""
    def random_player(board: list) -> int:
        return rng.choice(available_moves(board))
    return random_player


def run_demo(seed: int, demo_games: int) -> int:
    """Play scripted AI-vs-AI games and print each final board plus a tally."""
    rng = random.Random(seed)
    print("Cap-and-Trade Market Simulator: Terminal Game  (topic: Cap-and-Trade Market Simulator, seed=%d)" % seed)
    print("Scripted demo: %d tic-tac-toe games, AI (minimax) vs random\n" % demo_games)
    tally = {"X": 0, "O": 0, "draw": 0}
    for game in range(1, demo_games + 1):
        random_player = make_random_player(random.Random(seed + game))
        if game % 2 == 1:
            result, moves = play_game(ai_player, random_player)
            desc = "AI(X) vs random(O)"
        else:
            result, moves = play_game(random_player, ai_player)
            desc = "random(X) vs AI(O)"
        tally[result] += 1
        board = new_board()
        for player, move in moves:
            board[move] = player
        print("Game %d: %s -> %s in %d moves" % (game, desc, result, len(moves)))
        print(render(board))
        print()
    print("Tally over %d games: X wins %d, O wins %d, draws %d." % (
        demo_games, tally["X"], tally["O"], tally["draw"]))
    return 0


def run_play() -> int:
    """Interactive mode: you are X, the minimax AI is O."""
    print("Cap-and-Trade Market Simulator: Terminal Game - you play X, the AI plays O.")
    print("Enter a cell 0-8 (0=top-left, 8=bottom-right), or q to quit.\n")
    board = new_board()
    while winner(board) is None:
        print(render(board))
        raw = input("Your move (0-8): ").strip().lower()
        if raw == "q":
            print("Good game - quitting.")
            return 0
        try:
            move = int(raw)
        except ValueError:
            move = -1
        if move not in available_moves(board):
            print("Illegal move - pick an empty cell 0-8.")
            continue
        board[move] = "X"
        if winner(board) is not None:
            break
        board[ai_player(list(board))] = "O"
    print(render(board))
    result = winner(board)
    print({"X": "You win!", "O": "The AI wins.", "draw": "Draw."}[result])
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the demo."""
    parser = argparse.ArgumentParser(
        description="Cap-and-Trade Market Simulator: Terminal Game: Cap-and-trade sets a total emissions cap and lets firms buy and sell allowances, so the allowance price emerges where supply meets demand. The simulator runs trading rounds among firms with different abatement costs to find the clearing price."
    )
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for the demo (default: 42).")
    parser.add_argument("--play", action="store_true",
                        help="Play interactively against the AI via input().")
    parser.add_argument("--games", type=int, default=None,
                        help="Scripted demo games (see the topic params).")
    return parser


def main(argv=None) -> int:
    """Entry point: scripted demo by default, --play for interactive mode."""
    args = build_parser().parse_args(argv)
    random.seed(args.seed)
    if args.play:
        return run_play()
    games = args.games or int(PARAMS.get("demo_games", 4))
    return run_demo(args.seed, games)


if __name__ == "__main__":
    raise SystemExit(main())
