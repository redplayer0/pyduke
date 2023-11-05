import pyxel

TILE = 32


class Board:
    def __init__(self):
        self.rows = 6
        self.cols = 6
        self.positions = [[None for _ in range(6)] for _ in range(6)]
        self.line_length = self.rows * TILE

    def get_piece_position(self, name, id):
        for x, row in enumerate(self.positions):
            for y, piece in enumerate(row):
                if piece:
                    if piece.id == id and piece.name.upper() == name.upper():
                        return (x, y)

    def get_piece(self, x, y):
        return self.positions[x][y]

    def place_piece(self, x, y, piece):
        self.positions[x][y] = piece

    def draw(self):
        tile = TILE
        for row in range(self.rows):
            for col in range(self.cols):
                # row
                pyxel.line(
                    row * tile,
                    col * tile,
                    row * tile,
                    self.line_length,
                    pyxel.COLOR_DARK_BLUE,
                )
                # col
                pyxel.line(
                    row * tile,
                    col * tile,
                    self.line_length,
                    col * tile,
                    pyxel.COLOR_DARK_BLUE,
                )
        pyxel.line(
            self.rows * tile,
            0,
            self.line_length,
            self.cols * tile,
            pyxel.COLOR_DARK_BLUE,
        )
        pyxel.line(
            0,
            self.cols * tile,
            self.rows * tile,
            self.line_length,
            pyxel.COLOR_DARK_BLUE,
        )

    def draw_pieces(self):
        for x, row in enumerate(self.positions):
            for y, piece in enumerate(row):
                if piece:
                    piece.draw(x, y)
