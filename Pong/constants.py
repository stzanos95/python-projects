import random


# Screen constants
MAX_WIDTH = 800
MAX_HEIGHT = 600
PONG_TITLE = "PONG"
BACKCOL = "black"

# Scoreboard constants
FONT = ("Arial", 23, "bold")
ALIGNMENT = "center"

# Paddle constants
MOVE_DISTANCE = 20
PADDLE_WIDTH = 5
PADDLE_LENGTH = 1
PADDLE_Y = 0
PADDLE_X_RIGHT = 350
PADDLE_X_LEFT = -350

# Ball
DIR_ANGLES = [random.randint(20, 40),
              random.randint(50, 70),
              random.randint(110, 130),
              random.randint(140, 160),
              random.randint(200, 220),
              random.randint(230, 240),
              random.randint(280, 300),
              random.randint(310, 330)]
BOUNCE_DB = 20
