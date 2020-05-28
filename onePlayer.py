# Library import
from random import randint

import kivy
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.popup import Popup

from ai import Ai


class OnePlayerScreen(Screen):
    print(kivy.__version__)
    WINDOW_MIN_WIDTH = 640
    WINDOW_MIN_HEIGHT = 360

    font_scaling = NumericProperty()

    def on_size(self, *args):
        self.font_scaling = min(Window.width / self.WINDOW_MIN_WIDTH, Window.height / self.WINDOW_MIN_HEIGHT)

    # Variable setup
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

    def init_players(self):
        self.ai = Ai(self.letter[randint(0, 1)]);
        self.player = "X" if self.ai.letter == "O" else "O"
        turn = randint(0, 1)
        if turn == 1:
            self.ai.make_ai_move(self.board, self.winning_positions)
            #greeting = "Hello Player! Computer plays first! You are playing with \"" + self.player + "\""
        #else:
           # greeting = "Hello Player! You are playing with \"" + self.player + "\""
       # self.popup_message(greeting)

    # Main layout setup
    def __init__(self, **kwargs):
        super(OnePlayerScreen, self).__init__(**kwargs)
        self.layout = GridLayout(cols=3, rows=4)
        self.layout.spacing = [10, 10]
        self.layout.padding = [10, 10, 10, 10]
        self.add_widget(self.layout)

        # Create  3×3 grid
        for i in range(9):
            btn = Button(id=str(i), text=' ', font_size=120, on_press=self.click_box,
                         background_color=(0.16, 0.22, 0.298, 0.95), disabled_color=(0.16, 0.22, 0.298, 1),
                         background_disabled_normal='background.jpg', background_normal='background.jpg')
            self.board.append(btn)
            self.layout.add_widget(btn)

        # X's scoring
        self.x_wins = Label(bold=True, font_size=120, text='X: ' + str(self.x_points), color=(0.83, 0.36, 0.64, 1))
        self.layout.add_widget(self.x_wins)

        # O's scoring
        self.o_wins = Label(font_size=120, text='O: ' + str(self.o_points), color=(0.83, 0.36, 0.64, 1))
        self.layout.add_widget(self.o_wins)

        # Reset board & restart game menu
        self.reset_choices = GridLayout(cols=1, rows=2)
        self.reset_choices.spacing = [10, 10]
        self.reset_choices.padding = [10, 10, 10, 10]

        # reset board button
        reset_board_btn = Button(font_size=70, text='Reset Board', on_press=self.reset_board,
                                 background_color=(0.16, 0.22, 0.298, 1), disabled_color=(0.16, 0.22, 0.298, 1),
                                 background_disabled_normal='background.jpg', background_normal='background.jpg')

        # restart game button
        reset_game_btn = Button(font_size=70, text='Restart Game', on_press=self.reset_game,
                                background_color=(0.16, 0.22, 0.298, 1), disabled_color=(0.16, 0.22, 0.298, 1),
                                background_disabled_normal='background.jpg', background_normal='background.jpg')
        self.reset_choices.add_widget(reset_board_btn)
        self.reset_choices.add_widget(reset_game_btn)
        self.layout.add_widget(self.reset_choices)

    def popup_results(self, result):
        popup = Popup(title="GAME RESULTS:", content=Label(text=result), size=(400, 200), size_hint=(None, None))
        popup.bind(on_dismiss=self.reset_board)
        popup.open()

    # When a move is made
    def click_box(self, button):
        # If the board is full, we declare the result as 'tie' and reset the board
        if self.filledBox >= 8:
            self.popup_results('Its tie!')

        # if its 'Xs' turn
        elif self.turn == "X" and button.text == " ":
            button.text = "X"
            self.filledBox += 1
            self.turn = "O"  # its "Os" move
            self.o_wins.bold = True  # its 'Os' move so becomes bold
            self.x_wins.bold = False
            self.check_win()  # check winner after every move

        # if its 'Os' turn
        elif self.turn == "O" and button.text == " ":
            button.text = "O"
            self.filledBox += 1
            self.turn = "X"  # its "Xs" move
            self.x_wins.bold = True  # its 'Xs' move so becomes bold
            self.o_wins.bold = False
            self.check_win()  # check winner after every move

    # When the reset board button is clicked delete all values on the board
    def reset_board(self, button):
        self.filledBox = 0
        for button in self.board:
            button.text = " "
            button.disabled = False
            button.color = (1, 1, 1, 1)
            button.background_color = (0.16, 0.22, 0.298, 0.95)
            button.disabled_color = (0.16, 0.22, 0.298, 0.95)
            button.background_disabled_normal = 'background.jpg'
            button.background_normal = 'background.jpg'

    # If anyone has won
    def win(self, btn1, btn2, btn3):
        btn1.color = (0.96, 0.54, 0.25, 1)
        btn2.color = (0.96, 0.54, 0.25, 1)
        btn3.color = (0.96, 0.54, 0.25, 1)
        for button in self.board:
            if button != btn1 and button != btn2 and button != btn3:
                button.disabled = True
                button.background_disabled_normal = ''
                button.background_normal = ''
                button.background_color = (0.16, 0.22, 0.298, 0.95)
                button.disabled_color = (1, 1, 1, 1)

    # Checks if anyone has won
    def check_win(self):
        for trio in self.winning_positions:
            if self.board[trio[0]].text == "X" and self.board[trio[1]].text == "X" and self.board[trio[2]].text == "X":
                self.popup_results('X wins this round!')
                self.x_points += 1
                self.x_wins.text = 'X: ' + str(self.x_points)
                self.win(self.board[trio[0]], self.board[trio[1]], self.board[trio[2]])
            if self.board[trio[0]].text == "O" and self.board[trio[1]].text == "O" and self.board[trio[2]].text == "O":
                self.popup_results('O wins this round!')
                self.o_points += 1
                self.o_wins.text = 'O: ' + str(self.o_points)
                self.win(self.board[trio[0]], self.board[trio[1]], self.board[trio[2]])

    # When the restart game button is clicked reset all points to 0
    def reset_game(self, button):
        for button in self.board:
            button.text = " "
            button.disabled = False
            button.color = (1, 1, 1, 1)
        self.filledBox = 0
        self.o_points = 0
        self.x_points = 0
        self.o_wins.text = 'O: ' + str(self.o_points)
        self.x_wins.text = 'X: ' + str(self.x_points)

