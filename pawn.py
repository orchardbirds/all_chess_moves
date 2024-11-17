from board import SQUARES, PIECES
from captures import capture_pawnly, add_checks

PAWN_NORMAL_MOVES = {
    square for square in SQUARES if square[1] != "8" and square[1] != "1"
}


def pawn_promotions(squares: set[str]) -> set[str]:
    moves = {square for square in squares if square[1] == "8" or square[1] == "1"}
    possible_promotions = {piece for piece in PIECES if piece != "K"}

    return {move + piece for move in moves for piece in possible_promotions}


def pawn_captures(squares: set[str]) -> set[str]:
    return {capture for square in squares for capture in capture_pawnly(square)}


def pawn_caputure_promotions(squares: set[str]) -> set[str]:
    possible_promotions = {piece for piece in PIECES if piece != "K"}
    moves = {capture for square in squares for capture in capture_pawnly(square)}
    moves = {move for move in moves if move[3] == "8" or move[3] == "1"}
    return {move + piece for move in moves for piece in possible_promotions}


ALL_PAWN_MOVES = add_checks(
    PAWN_NORMAL_MOVES
    | pawn_promotions(SQUARES)
    | pawn_captures(PAWN_NORMAL_MOVES)
    | pawn_caputure_promotions(SQUARES)
)
