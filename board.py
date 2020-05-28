import kivy
from kivy.properties import NumericProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window


class Board:
    WINDOW_MIN_WIDTH = 640
    WINDOW_MIN_HEIGHT = 360

    font_scaling = NumericProperty()

    def on_size(self, *args):
        self.font_scaling = min(Window.width / self.WINDOW_MIN_WIDTH, Window.height / self.WINDOW_MIN_HEIGHT)

    # Variable setup
    turn = "X"
    filledBox = 0
    x_points = 0
    o_points = 0
    x_wins = Label()
    o_wins = Label()
    winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal win
                         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical win
                         [0, 4, 8], [2, 4, 6]  # Diagonal win
                         ]
    board = list()
