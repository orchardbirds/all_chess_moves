from board import SQUARES
from captures import add_checks

KING_NORMAL_MOVES = {"K" + square for square in SQUARES}
KING_CASTLING_MOVES = {"O-O", "O-O-O"}
KING_CAPTURES = {"Kx" + square for square in SQUARES}

ALL_KING_MOVES = add_checks(KING_NORMAL_MOVES | KING_CASTLING_MOVES | KING_CAPTURES)
