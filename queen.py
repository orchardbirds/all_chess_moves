from board import SQUARES, FILES, RANKS
from captures import (
    capture_horizontally,
    capture_vertically,
    capture_diagonally,
    add_checks,
)

QUEEN_NORMAL_MOVES = {"Q" + square for square in SQUARES}
QUEEN_NORMAL_CAPTURES = {"Qx" + square for square in SQUARES}


def queen_single_disambiguation(squares: set[str]) -> set[str]:
    disambiguation_rank = {"Q" + rank + square for rank in RANKS for square in squares}
    disambiguation_file = {"Q" + file + square for file in FILES for square in squares}
    return disambiguation_rank | disambiguation_file


def queen_single_disambiguation_captures(squares: set[str]) -> set[str]:
    disambiguation_rank = {
        "Q" + rank + "x" + square for rank in RANKS for square in squares
    }
    disambiguation_file = {
        "Q" + file + "x" + square for file in FILES for square in squares
    }
    return disambiguation_rank | disambiguation_file


def queen_double_disambiguation(squares: set[str]) -> set[str]:
    possible_squares_horizontal = {
        "Q" + square + x for x in squares for square in capture_horizontally(x)
    }
    possible_squares_vertical = {
        "Q" + square + x for x in squares for square in capture_vertically(x)
    }
    possible_squares_diagonal = {
        "Q" + square + x for x in squares for square in capture_diagonally(x)
    }
    return (
        possible_squares_horizontal
        | possible_squares_vertical
        | possible_squares_diagonal
    )


def queen_double_disambiguation_captures(squares: set[str]) -> set[str]:
    possible_squares_horizontal = {
        "Q" + square + "x" + x for x in squares for square in capture_horizontally(x)
    }
    possible_squares_vertical = {
        "Q" + square + "x" + x for x in squares for square in capture_vertically(x)
    }
    possible_squares_diagonal = {
        "Q" + square + "x" + x for x in squares for square in capture_diagonally(x)
    }
    return (
        possible_squares_horizontal
        | possible_squares_vertical
        | possible_squares_diagonal
    )


ALL_QUEEN_MOVES = add_checks(
    QUEEN_NORMAL_MOVES
    | QUEEN_NORMAL_CAPTURES
    | queen_single_disambiguation(SQUARES)
    | queen_single_disambiguation_captures(SQUARES)
    | queen_double_disambiguation(SQUARES)
    | queen_double_disambiguation_captures(SQUARES)
)
