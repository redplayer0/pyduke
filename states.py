import pyxel
from core import calculate_spawn_positions
from core import calculate_moves

TILE = 32


class SetupState:
    def __init__(self, game):
        self.game = game
        self.possible_positions = []

    def update(self):
        game = self.game
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and not game.in_hand:
            game.in_hand = game.cur_player.get_initial_piece()
            self.possible_positions = calculate_spawn_positions(
                game.in_hand, game.board
            )
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and game.in_hand:
            x = pyxel.mouse_x // 32
            y = pyxel.mouse_y // 32
            if (x, y) in self.possible_positions:
                game.board.place_piece(x, y, game.in_hand)
                game.in_hand = None
                self.possible_positions = []
                if len(game.cur_player.initial_pieces) == 0:
                    game.next_player()
                    if game.cur_player.initial_pieces == []:
                        game.finish_setup()
                else:
                    game.in_hand = game.cur_player.get_initial_piece()
                    self.possible_positions = calculate_spawn_positions(
                        game.in_hand, game.board
                    )

    def draw(self):
        game = self.game
        # draw possible positions
        for tile in self.possible_positions:
            pyxel.rect(
                tile[0] * TILE + 1,
                tile[1] * TILE + 1,
                TILE - 1,
                TILE - 1,
                pyxel.COLOR_LIGHT_BLUE,
            )
        # draw piece in hand
        if game.in_hand:
            game.in_hand.drag(pyxel.mouse_x, pyxel.mouse_y)


class PlayerTurnState:
    def __init__(self, game):
        self.game = game
        self.possible_positions = []
        self.highlight = None
        self.target = None
        self.phase = "standby"
        self.phases = [
            "standby",
            "spawning",
            "acting",
            "end",
        ]

    def update(self):
        game = self.game
        board = self.game.board
        x = pyxel.mouse_x // 32
        y = pyxel.mouse_y // 32
        piece = game.board.get_piece(x, y)

        match self.phase:
            case "standby":
                # debug
                if pyxel.btnp(pyxel.MOUSE_BUTTON_MIDDLE):
                    self.phase = "end"
                    return

                # RIGHT CLICK
                if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
                    game.in_hand = game.cur_player.pull_piece()
                    if game.in_hand:
                        self.possible_positions = calculate_spawn_positions(
                            game.in_hand, game.board
                        )
                        self.phase = "spawning"
                        return
                    else:
                        return

                # LEFT CLICK
                if (
                    pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)
                    and not game.active
                    and piece
                    and piece.id == game.cur_player.id
                ):
                    self.possible_positions = calculate_moves(x, y, piece, board)
                    if len(self.possible_positions) > 0:
                        game.active = piece
                        self.highlight = (x, y)
                        self.phase = "acting"
                        return

            case "spawning":
                if (
                    pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)
                    and (x, y) in self.possible_positions
                ):
                    board.place_piece(x, y, game.in_hand)
                    game.in_hand = None
                    self.possible_positions = []
                    game.next_player()
                    self.phase = "standby"
                    return

            case "acting":
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    if (x, y) in self.possible_positions:
                        # TODO make this better
                        board.place_piece(x, y, game.active)
                        game.active.flip()
                        board.positions[self.highlight[0]][self.highlight[1]] = None
                        self.highlight = None
                        game.active = None
                        self.possible_positions = []
                        game.next_player()
                        self.phase = "standby"
                        return
                    else:
                        game.active = None
                        self.highlight = None
                        self.possible_positions = []
                        self.phase = "standby"
                        return

    def draw(self):
        game = self.game
        # draw possible positions
        for tile in self.possible_positions:
            piece = game.board.get_piece(tile[0], tile[1])
            if piece and piece.id != game.active.id:
                pyxel.rectb(
                    tile[0] * TILE,
                    tile[1] * TILE,
                    TILE + 1,
                    TILE + 1,
                    pyxel.COLOR_YELLOW,
                )
            else:
                pyxel.rect(
                    tile[0] * TILE + 1,
                    tile[1] * TILE + 1,
                    TILE - 1,
                    TILE - 1,
                    pyxel.COLOR_LIGHT_BLUE,
                )
        # draw highlight
        if self.highlight:
            pyxel.rectb(
                self.highlight[0] * TILE + 1,
                self.highlight[1] * TILE + 1,
                TILE - 1,
                TILE - 1,
                pyxel.COLOR_YELLOW,
            )

        if self.phase == "end":
            pyxel.text(62, 80, f"---> THE END <---", pyxel.COLOR_YELLOW)

        # draw piece in hand
        if game.in_hand:
            game.in_hand.drag(pyxel.mouse_x, pyxel.mouse_y)

        #     # debug
        #     pyxel.text(
        #         0, 180, f"spawn points: {self.possible_positions}", pyxel.COLOR_YELLOW
        #     )
        #
        # # debug
        # pyxel.text(0, 170, f"phase: {self.phase}", pyxel.COLOR_YELLOW)
