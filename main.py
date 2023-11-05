import pyxel

from board import Board
from piece import Piece
from player import Player
from states import SetupState
from states import PlayerTurnState

TILE = 32
PLAYER_1 = 1
PLAYER_2 = 2


class Game:
    def __init__(self):
        # pyxel stuff
        pyxel.init(240, 240)
        pyxel.load("my_resource.pyxres")
        pyxel.mouse(True)

        self.board = Board()
        self.state = SetupState(self)

        self.in_hand = None
        self.active = None

        self.player_1 = Player(PLAYER_1)
        self.player_2 = Player(PLAYER_2)
        self.cur_player = self.player_1

        # self.possible_cells = []

        self.player_1.give_pieces(
            Piece("priest"),
            Piece("seer"),
        )

        self.player_2.give_pieces(
            Piece("foot"),
            Piece("foot"),
        )

        pyxel.run(self.update, self.draw)

    def finish_setup(self):
        self.state = PlayerTurnState(self)

    def next_player(self):
        if self.cur_player == self.player_1:
            self.cur_player = self.player_2
        else:
            self.cur_player = self.player_1

    def update(self):
        self.state.update()

    def draw(self):
        pyxel.cls(pyxel.COLOR_WHITE)
        self.board.draw()
        self.board.draw_pieces()
        self.state.draw()

        # debug info
        x = pyxel.mouse_x // 32
        y = pyxel.mouse_y // 32
        piece = self.board.get_piece(x, y)
        pyxel.text(
            0,
            0,
            f"active: {self.active.name if self.active else ''}",
            pyxel.COLOR_BLACK,
        )
        pyxel.text(
            0,
            10,
            f"under mouse: {piece.name if piece else ''}",
            pyxel.COLOR_BLACK,
        )

        # grid position
        pyxel.text(0, 20, f"x: {x} y: {y}", pyxel.COLOR_BLACK)

        pyxel.text(
            0,
            30,
            f"cur_player: {self.cur_player.id}",
            pyxel.COLOR_BLACK,
        )


Game()
