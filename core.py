from moves import SPAWN_POSITIONS


def load_pieces(filename):
    pieces = {}

    with open(filename, "r") as f:
        for line in f.readlines():
            parts = line.strip().split(":")
            name = parts[0].strip()
            parts = parts[1].strip().split("-")
            normal_moves = parts[0]
            flipped_moves = parts[1]

            pieces[name] = [normal_moves.split(), flipped_moves.split()]

    return pieces


def calculate_spawn_positions(piece, board):
    array = []
    if piece.name.upper() == "DUKE":
        return [(2, 5), (3, 5)] if piece.id == 1 else [(2, 0), (3, 0)]
    else:
        duke = board.get_piece_position("DUKE", piece.id)
        for move in SPAWN_POSITIONS:
            x = duke[0] + move.dx
            y = duke[1] + move.dy
            if 0 <= x < 6 and 0 <= y < 6:
                if not board.get_piece(x, y):
                    array.append((x, y))

    return array


def calculate_moves(px, py, piece, board):
    array = []

    for move in piece.moves:
        dx = move.dx if piece.id == 1 else -move.dx
        dy = move.dy if piece.id == 1 else -move.dy
        if move.is_slide:
            x = px + dx
            y = py + dy
            while 0 <= x < 6 and 0 <= y < 6:
                pos_piece = board.get_piece(x, y)
                if not pos_piece:
                    array.append((x, y))
                    x += dx
                    y += dy
                elif pos_piece.id != piece.id:
                    array.append((x, y))
                    break
                else:
                    break
        else:
            x = px + dx
            y = py + dy
            if 0 <= x < 6 and 0 <= y < 6:
                pos_piece = board.get_piece(x, y)
                if not pos_piece:
                    array.append((x, y))
                elif pos_piece.id != piece.id:
                    array.append((x, y))

    return array


PIECES = load_pieces("pieces.txt")
