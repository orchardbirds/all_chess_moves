from board import SQUARES, FILES, RANKS
from captures import add_checks

ROOK_NORMAL_MOVES = {"R" + square for square in SQUARES}
ROOK_NORMAL_CAPTURES = {"Rx" + square for square in SQUARES}

ROOK_DOUBLE_DISAMBIGUATION_EXCEPTION = {"a1", "a8", "h1", "h8"}


def rook_single_disambiguation(squares: set[str]) -> set[str]:
    disambiguation_rank = {"R" + rank + square for rank in RANKS for square in squares}
    disambiguation_file = {
        "R" + file + square for file in FILES for square in squares if file != square[1]
    }
    disambiguation_file = {
        disambiguation
        for disambiguation in disambiguation_file
        if _check_single_disambiguation(disambiguation, start=1, end=3)
    }
    return disambiguation_rank | disambiguation_file


def _check_single_disambiguation(disambiguation: str, start: int, end: int) -> bool:
    if disambiguation[start] == "2" and disambiguation[end] == "1":
        return False
    if disambiguation[start] == "7" and disambiguation[end] == "8":
        return False
    return True


def rook_single_disambiguation_captures(squares: set[str]) -> set[str]:
    disambiguations = rook_single_disambiguation(squares)
    disambiguations = {
        disambiguation.replace("R", "Rx") for disambiguation in disambiguations
    }

    return disambiguations


ALL_ROOK_MOVES = add_checks(
    ROOK_NORMAL_MOVES
    | ROOK_NORMAL_CAPTURES
    | rook_single_disambiguation(SQUARES)
    | rook_single_disambiguation_captures(SQUARES)
)
