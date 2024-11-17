from board import SQUARES, FILES, RANKS
from captures import capture_diagonally, add_checks

# We can't choose which bishop to put on these squares
BISHOP_SINGLE_AMBIGUATION_EXCEPTION_RANK = {"a1", "a8", "h1", "h8"}
BISHOP_SINGLE_AMBIGUATION_EXCEPTION_FILE = {
    "a1",
    "b1",
    "c1",
    "d1",
    "e1",
    "f1",
    "g1",
    "h1",
    "a8",
    "b8",
    "c8",
    "d8",
    "e8",
    "f8",
    "g8",
    "h8",
}

BISHOP_DOUBLE_AMBIGUATION_EXCEPTION = {
    "a1",
    "b1",
    "c1",
    "d1",
    "e1",
    "f1",
    "g1",
    "h1",
    "a8",
    "b8",
    "c8",
    "d8",
    "e8",
    "f8",
    "g8",
    "h8",
    "a2",
    "a3",
    "a4",
    "a5",
    "a6",
    "a7",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "h7",
}

BISHOP_NORMAL_MOVES = {"B" + square for square in SQUARES}
BISHOP_NORMAL_CAPTURES = {"Bx" + square for square in SQUARES}


def _is_allowed_file_disambiguations(disambiguation: str) -> bool:
    """
    Bishops are tricky. We can't have, e.g. B8b4.
    This functions removes all the disambiguations that are not allowed.
    """
    rank = int(disambiguation[1])
    final_rank = int(disambiguation[-1])

    if final_rank in [2, 7]:
        if rank in range(final_rank - 1, final_rank + 2):
            return True
        return False
    elif final_rank in [3, 6]:
        if rank in range(final_rank - 2, final_rank + 3):
            return True
        return False
    elif final_rank in [4, 5]:
        if rank in range(final_rank - 3, final_rank + 4):
            return True
        return False
    return False


def _is_allowed_double_disambiguations(disambiguation: str) -> bool:
    rank = int(disambiguation[2])
    final_rank = int(disambiguation[-1])
    final_square = disambiguation[-2:]

    if final_square in ["e4", "d5", "e5", "d4"]:
        if rank in range(final_rank - 3, final_rank + 4):
            return True
        return False
    elif final_square in [
        "c3",
        "c4",
        "c5",
        "c6",
        "d3",
        "d6",
        "e3",
        "e6",
        "f3",
        "f4",
        "f5",
        "f6",
    ]:
        if rank in range(final_rank - 2, final_rank + 3):
            return True
        return False
    else:
        if rank in range(final_rank - 1, final_rank + 2):
            return True
        return False


def bishop_single_disambiguation(squares: set[str]) -> set[str]:
    disambiguation_rank = {
        "B" + rank + square
        for rank in RANKS
        for square in squares
        if rank != square[0] and square not in BISHOP_SINGLE_AMBIGUATION_EXCEPTION_RANK
    }
    disambiguation_file = {
        "B" + file + square
        for file in FILES
        for square in squares
        if file != square[1] and square not in BISHOP_SINGLE_AMBIGUATION_EXCEPTION_FILE
    }
    disambiguation_file = {
        disambiguation
        for disambiguation in disambiguation_file
        if _is_allowed_file_disambiguations(disambiguation)
    }

    return disambiguation_rank | disambiguation_file


def bishop_single_disambiguation_captures(squares: set[str]) -> set[str]:
    disambiguation_rank = {
        "B" + rank + "x" + square
        for rank in RANKS
        for square in squares
        if rank != square[0] and square not in BISHOP_SINGLE_AMBIGUATION_EXCEPTION_RANK
    }
    disambiguation_file = {
        "B" + file + "x" + square
        for file in FILES
        for square in squares
        if file != square[1] and square not in BISHOP_SINGLE_AMBIGUATION_EXCEPTION_FILE
    }
    disambiguation_file = {
        disambiguation
        for disambiguation in disambiguation_file
        if _is_allowed_file_disambiguations(disambiguation)
    }
    return disambiguation_rank | disambiguation_file


def bishop_double_disambiguation(squares: set[str]) -> set[str]:
    disambiguations = {
        "B" + square + x
        for x in squares
        for square in capture_diagonally(x)
        if x not in BISHOP_DOUBLE_AMBIGUATION_EXCEPTION
    }
    return {
        disambiguation
        for disambiguation in disambiguations
        if _is_allowed_double_disambiguations(disambiguation)
    }


def bishop_double_disambiguation_captures(squares: set[str]) -> set[str]:
    disambiguations = {
        "B" + square + "x" + x
        for x in squares
        for square in capture_diagonally(x)
        if x not in BISHOP_DOUBLE_AMBIGUATION_EXCEPTION
    }
    return {
        disambiguation
        for disambiguation in disambiguations
        if _is_allowed_double_disambiguations(disambiguation)
    }


ALL_BISHOP_MOVES = add_checks(
    BISHOP_NORMAL_MOVES
    | BISHOP_NORMAL_CAPTURES
    | bishop_single_disambiguation(SQUARES)
    | bishop_single_disambiguation_captures(SQUARES)
    | bishop_double_disambiguation(SQUARES)
    | bishop_double_disambiguation_captures(SQUARES)
)
