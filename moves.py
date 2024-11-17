from pawn import ALL_PAWN_MOVES
from rook import ALL_ROOK_MOVES
from king import ALL_KING_MOVES
from knight import ALL_KNIGHT_MOVES
from bishop import ALL_BISHOP_MOVES
from queen import ALL_QUEEN_MOVES

ALL_MOVES = (
    ALL_PAWN_MOVES
    | ALL_ROOK_MOVES
    | ALL_KING_MOVES
    | ALL_KNIGHT_MOVES
    | ALL_BISHOP_MOVES
    | ALL_QUEEN_MOVES
)
