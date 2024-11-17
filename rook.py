from board import SQUARES, FILES, RANKS
from captures import capture_horizontally, capture_vertically, add_checks

ROOK_NORMAL_MOVES = {"R" + square for square in SQUARES}
ROOK_NORMAL_CAPTURES = {"Rx" + square for square in SQUARES}


def rook_single_disambiguation(squares: set[str]) -> set[str]:
    disambiguation_rank = {"R" + rank + square for rank in RANKS for square in squares}
    disambiguation_file = {"R" + file + square for file in FILES for square in squares}
    return disambiguation_rank | disambiguation_file


def rook_single_disambiguation_captures(squares: set[str]) -> set[str]:
    disambiguation_rank = {
        "R" + rank + "x" + square for rank in RANKS for square in squares
    }
    disambiguation_file = {
        "R" + file + "x" + square for file in FILES for square in squares
    }
    return disambiguation_rank | disambiguation_file


def rook_double_disambiguation(squares: set[str]) -> set[str]:
    possible_squares_horizontal = {
        "R" + square + x for x in squares for square in capture_horizontally(x)
    }
    possible_squares_vertical = {
        "R" + square + x for x in squares for square in capture_vertically(x)
    }
    return possible_squares_horizontal | possible_squares_vertical


def rook_double_disambiguation_captures(squares: set[str]) -> set[str]:
    possible_squares_horizontal = {
        "R" + square + "x" + x for x in squares for square in capture_horizontally(x)
    }
    possible_squares_vertical = {
        "R" + square + "x" + x for x in squares for square in capture_vertically(x)
    }
    return possible_squares_horizontal | possible_squares_vertical


ALL_ROOK_MOVES = add_checks(
    ROOK_NORMAL_MOVES
    | ROOK_NORMAL_CAPTURES
    | rook_single_disambiguation(SQUARES)
    | rook_single_disambiguation_captures(SQUARES)
    | rook_double_disambiguation(SQUARES)
    | rook_double_disambiguation_captures(SQUARES)
)
