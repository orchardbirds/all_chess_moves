from board import SQUARES
from captures import capture_knightly, add_checks

KNIGHT_NORMAL_MOVES = {"N" + square for square in SQUARES}
KNIGHT_NORMAL_CAPTURES = {"Nx" + square for square in SQUARES}

# We can't have, e.g. N6h8
KNIGHT_SINGLE_DISAMBIGUATION_FILE_EXCEPTIONS = {
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

# Same as above but for when we need to have a rank disambiguation as well with at least 3 knights on the board
KNIGHT_DOUBLE_DISAMBIGUATION_EXCEPTIONS = {
    "a1",
    "a2",
    "a3",
    "a4",
    "a5",
    "a6",
    "a7",
    "a8",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "h7",
    "h8",
    "b1",
    "c1",
    "d1",
    "e1",
    "f1",
    "g1",
    "h1",
    "b8",
    "c8",
    "d8",
    "e8",
    "f8",
    "g8",
    "h8",
    "b2",
    "b7",
    "g2",
    "g7",
}


def knight_single_disambiguation(squares: set[str]) -> set[str]:
    possible_squares_knightly_rank = {
        "N" + square[0] + x for x in squares for square in capture_knightly(x)
    }
    possible_squares_knightly_file = {
        "N" + square[1] + x
        for x in squares
        for square in capture_knightly(x)
        if x not in KNIGHT_SINGLE_DISAMBIGUATION_FILE_EXCEPTIONS
    }
    return possible_squares_knightly_file | possible_squares_knightly_rank


def knight_single_disambiguation_captures(squares: set[str]) -> set[str]:
    possible_squares_knightly_rank = {
        "N" + square[0] + "x" + x for x in squares for square in capture_knightly(x)
    }
    possible_squares_knightly_file = {
        "N" + square[1] + "x" + x
        for x in squares
        for square in capture_knightly(x)
        if x not in KNIGHT_SINGLE_DISAMBIGUATION_FILE_EXCEPTIONS
    }
    return possible_squares_knightly_file | possible_squares_knightly_rank


def knight_double_disambiguation(squares: set[str]) -> set[str]:
    return {
        "N" + square + x
        for x in squares
        for square in capture_knightly(x)
        if x not in KNIGHT_DOUBLE_DISAMBIGUATION_EXCEPTIONS
    }


def knight_double_disambiguation_captures(squares: set[str]) -> set[str]:
    return {
        "N" + square + "x" + x
        for x in squares
        for square in capture_knightly(x)
        if x not in KNIGHT_DOUBLE_DISAMBIGUATION_EXCEPTIONS
    }


ALL_KNIGHT_MOVES = add_checks(
    KNIGHT_NORMAL_MOVES
    | KNIGHT_NORMAL_CAPTURES
    | knight_single_disambiguation(SQUARES)
    | knight_single_disambiguation_captures(SQUARES)
    | knight_double_disambiguation(SQUARES)
    | knight_double_disambiguation_captures(SQUARES)
)
