class Move:
    def __init__(self, dx, dy, is_slide=False, is_jump=False, is_strike=False, is_command=False, is_shield=False):
        self.dx = dx
        self.dy = dy
        self.is_slide = is_slide
        self.is_jump = is_jump
        self.is_strike = is_strike
        self.is_command = is_command
        self.is_shield = is_shield


MOVES = {
    # ORTHO MOVES
    "UP": Move(0, -1),
    "DOWN": Move(0, 1),
    "LEFT": Move(-1, 0),
    "RIGHT": Move(1, 0),
    "UP2": Move(0, -2),
    # DIAG MOVES
    "UP_LEFT": Move(-1, -1),
    "DOWN_LEFT": Move(-1, 1),
    "UP_RIGHT": Move(1, -1),
    "DOWN_RIGHT": Move(1, 1),
    # ORTHO JUMPS
    "JUMP_UP": Move(0, -2, is_jump=True),
    "JUMP_DOWN": Move(0, 2, is_jump=True),
    "JUMP_LEFT": Move(-2, 0, is_jump=True),
    "JUMP_RIGHT": Move(2, 0, is_jump=True),
    # ORTHO SLIDES
    "SLIDE_UP": Move(0, -1, is_slide=True),
    "SLIDE_DOWN": Move(0, 1, is_slide=True),
    "SLIDE_LEFT": Move(-1, 0, is_slide=True),
    "SLIDE_RIGHT": Move(1, 0, is_slide=True),
}

SPAWN_POSITIONS = [
        MOVES["UP"],
        MOVES["DOWN"],
        MOVES["LEFT"],
        MOVES["RIGHT"],
        ]

def create_move(move):
    dx = 0
    dy = 0

    is_slide = False
    is_strike = False
    is_jump = False
    is_command = False
    is_shield = False
    
    if "u" in move:
        dy -= 1
    if "d" in move:
        dy += 1
    if "l" in move:
        dx -= 1
    if "r" in move:
        dx += 1

    if "s" in move:
        is_slide = True
    if "j" in move:
        is_jump = True
    if "k" in move:
        is_strike = True
    if "c" in move:
        is_command = True
    if "h" in move:
        is_shield = True

    if "2" in move:
        dx = dx*2
        dy = dy*2

    return Move(dx, dy, is_slide, is_jump, is_strike, is_command, is_shield)
