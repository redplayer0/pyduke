import pyxel

from core import load_pieces
from moves import create_move

TILE = 32
PIECES = load_pieces("pieces.txt")


class Piece:
    def __init__(self, name, id=None):
        self.id = id
        if id == 2:
            self.name = name.upper()
        else:
            self.name = name
        self.is_flipped = False
        self.is_hover = False
        self.normal_moves = []
        self.flipped_moves = []
        for move in PIECES[name][0]:
            self.normal_moves.append(create_move(move))
        for move in PIECES[name][1]:
            self.flipped_moves.append(create_move(move))
        self.moves = self.normal_moves

    def flip(self):
        if self.is_flipped:
            self.is_flipped = False
            self.moves = self.normal_moves
        else:
            self.is_flipped = True
            self.moves = self.flipped_moves

    def draw(self, x, y):
        if self.id == 1:
            pyxel.blt(x * TILE + 1, y * TILE + 1, 0, 0, 0, TILE - 1, TILE - 1)
        else:
            pyxel.blt(x * TILE + 1, y * TILE + 1, 0, 0, 32, TILE - 1, TILE - 1)
        for move in self.moves:
            dx = move.dx
            dy = move.dy
            if self.id == 2:
                dx = -dx
                dy = -dy
            if move.is_slide and move.is_jump:
                pyxel.rect(
                    x * TILE + 1 + 15 + dx * 5,
                    y * TILE + 1 + 15 + dy * 5,
                    2,
                    2,
                    pyxel.COLOR_WHITE,
                )
                pyxel.rectb(
                    x * TILE + 1 + 14 + dx * 5,
                    y * TILE + 1 + 14 + dy * 5,
                    4,
                    4,
                    pyxel.COLOR_BLACK,
                )
            elif move.is_jump:
                pyxel.rectb(
                    x * TILE + 1 + 14 + dx * 5,
                    y * TILE + 1 + 14 + dy * 5,
                    4,
                    4,
                    pyxel.COLOR_BLACK,
                )
            elif move.is_slide:
                pyxel.rect(
                    x * TILE + 1 + 15 + dx * 5,
                    y * TILE + 1 + 15 + dy * 5,
                    2,
                    2,
                    pyxel.COLOR_WHITE,
                )
            else:
                pyxel.rect(
                    x * TILE + 1 + 15 + dx * 5,
                    y * TILE + 1 + 15 + dy * 5,
                    2,
                    2,
                    pyxel.COLOR_BLACK,
                )

    def drag(self, x, y):
        if self.id == 1:
            pyxel.blt(x, y, 0, 0, 0, TILE - 1, TILE - 1)
        else:
            pyxel.blt(x, y, 0, 0, 32, TILE - 1, TILE - 1)
        for move in self.moves:
            dx = move.dx
            dy = move.dy
            if self.id == 2:
                dx = -dx
                dy = -dy
            if move.is_slide and move.is_jump:
                pyxel.rect(
                    x + 15 + dx * 5,
                    y + 15 + dy * 5,
                    2,
                    2,
                    pyxel.COLOR_WHITE,
                )
                pyxel.rectb(
                    x + 14 + dx * 5,
                    y + 14 + dy * 5,
                    4,
                    4,
                    pyxel.COLOR_BLACK,
                )
            elif move.is_jump:
                pyxel.rectb(
                    x + 14 + dx * 5,
                    y + 14 + dy * 5,
                    4,
                    4,
                    pyxel.COLOR_BLACK,
                )
            elif move.is_slide:
                pyxel.rect(
                    x + 15 + dx * 5,
                    y + 15 + dy * 5,
                    2,
                    2,
                    pyxel.COLOR_WHITE,
                )
            else:
                pyxel.rect(
                    x + 15 + dx * 5,
                    y + 15 + dy * 5,
                    2,
                    2,
                    pyxel.COLOR_BLACK,
                )
