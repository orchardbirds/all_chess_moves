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
    disambiguation_file = {
        "Q" + file + square for file in FILES for square in squares if file != square[1]
    }
    return disambiguation_rank | disambiguation_file


def queen_single_disambiguation_captures(squares: set[str]) -> set[str]:
    disambiguation_rank = {
        "Q" + rank + "x" + square for rank in RANKS for square in squares
    }
    disambiguation_file = {
        "Q" + file + "x" + square
        for file in FILES
        for square in squares
        if file != square
    }
    return disambiguation_rank | disambiguation_file


def _is_allowed_double_disambiguations(
    disambiguation: str, disambiguation_indices: tuple[int, int] = (3, 5)
) -> bool:
    start, finish = disambiguation_indices
    if disambiguation[start:finish] == "a1":
        if disambiguation[2] == "1":
            return False
        if disambiguation[1] == "a":
            return False
    elif disambiguation[start:finish] == "a8":
        if disambiguation[2] == "8":
            return False
        if disambiguation[1] == "a":
            return False
    elif disambiguation[start:finish] == "h1":
        if disambiguation[2] == "1":
            return False
        if disambiguation[1] == "h":
            return False
    elif disambiguation[start:finish] == "h8":
        if disambiguation[2] == "8":
            return False
        if disambiguation[1] == "h":
            return False
    return True


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
    disambiguations = (
        possible_squares_diagonal
        | possible_squares_horizontal
        | possible_squares_vertical
    )
    return {
        disambiguation
        for disambiguation in disambiguations
        if _is_allowed_double_disambiguations(
            disambiguation, disambiguation_indices=(3, 5)
        )
    }


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
    disambiguations = (
        possible_squares_diagonal
        | possible_squares_horizontal
        | possible_squares_vertical
    )
    return {
        disambiguation
        for disambiguation in disambiguations
        if _is_allowed_double_disambiguations(
            disambiguation, disambiguation_indices=(4, 6)
        )
    }


ALL_QUEEN_MOVES = add_checks(
    QUEEN_NORMAL_MOVES
    | QUEEN_NORMAL_CAPTURES
    | queen_single_disambiguation(SQUARES)
    | queen_single_disambiguation_captures(SQUARES)
    | queen_double_disambiguation(SQUARES)
    | queen_double_disambiguation_captures(SQUARES)
)
