from board import SQUARES


def capture_diagonally(square):
    file, rank = square
    file_index = ord(file) - ord("a")
    rank_index = int(rank) - 1

    captures = []

    for i in range(1, 8):
        if rank_index + i < 8 and file_index + i < 8:
            captures.append(chr(ord(file) + i) + str(int(rank) + i))
        if rank_index - i >= 0 and file_index + i < 8:
            captures.append(chr(ord(file) + i) + str(int(rank) - i))
        if rank_index + i < 8 and file_index - i >= 0:
            captures.append(chr(ord(file) - i) + str(int(rank) + i))
        if rank_index - i >= 0 and file_index - i >= 0:
            captures.append(chr(ord(file) - i) + str(int(rank) - i))

    return captures


def capture_horizontally(square):
    file, rank = square
    file_index = ord(file) - ord("a")

    captures = []

    for i in range(1, 8):
        if file_index + i < 8:
            captures.append(chr(ord(file) + i) + rank)
        if file_index - i >= 0:
            captures.append(chr(ord(file) - i) + rank)

    return captures


def capture_vertically(square):
    file, rank = square
    rank_index = int(rank) - 1

    captures = []

    for i in range(1, 8):
        if rank_index + i < 8:
            captures.append(file + str(int(rank) + i))
        if rank_index - i >= 0:
            captures.append(file + str(int(rank) - i))

    return captures


def capture_knightly(square):
    file, rank = square
    file_index = ord(file) - ord("a")
    rank_index = int(rank) - 1

    captures = []

    for i in range(1, 3):
        if rank_index + i < 8:
            if file_index + 3 - i < 8:
                captures.append(chr(ord(file) + 3 - i) + str(int(rank) + i))
            if file_index - 3 + i >= 0:
                captures.append(chr(ord(file) - 3 + i) + str(int(rank) + i))
        if rank_index - i >= 0:
            if file_index + 3 - i < 8:
                captures.append(chr(ord(file) + 3 - i) + str(int(rank) - i))
            if file_index - 3 + i >= 0:
                captures.append(chr(ord(file) - 3 + i) + str(int(rank) - i))

    return captures


def capture_pawnly(square):
    file, rank = square
    file_index = ord(file) - ord("a")
    rank_index = int(rank) - 1

    captures = []

    if rank_index + 1 < 8:
        if file_index + 1 < 8:
            captures.append(chr(ord(file) + 1) + str(int(rank) + 1))
        if file_index - 1 >= 0:
            captures.append(chr(ord(file) - 1) + str(int(rank) + 1))

    if rank_index - 1 >= 0:
        if file_index + 1 < 8:
            captures.append(chr(ord(file) + 1) + str(int(rank) - 1))
        if file_index - 1 >= 0:
            captures.append(chr(ord(file) - 1) + str(int(rank) - 1))

    return [file + "x" + capture for capture in captures]


def add_checks(moves: set[str]) -> set[str]:
    moves_check = {move + "+" for move in moves}
    moves_checkmate = {move + "#" for move in moves}
    return moves | moves_check | moves_checkmate


DIAGONAL_CAPTURES = {square: capture_diagonally(square) for square in SQUARES}
HORIZONTAL_CAPTURES = {square: capture_horizontally(square) for square in SQUARES}
VERTICAL_CAPTURES = {square: capture_vertically(square) for square in SQUARES}
KNIGHTLY_CAPTURES = {square: capture_knightly(square) for square in SQUARES}
