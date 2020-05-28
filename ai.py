from onePlayer import OnePlayerScreen


class Ai:
    def __init__(self, letter):
        self.letter = letter

    def check_if_win(self, board, winning_positions, move):
        current_move = move
        for trio in winning_positions:
            if board[trio[0]].text == self.letter and board[trio[1]].text == self.letter and board[trio[2]].text == self.letter:
                current_move = True
        return current_move

    def check_if_lose(self, board, winning_positions, move):
        current_move = move
        if self.letter == "X":
            for trio in winning_positions:
                if board[trio[0]].text == "O" and board[trio[1]].text == "O" and board[trio[2]].text == "O":
                    current_move = True
        else:
            for trio in winning_positions:
                if board[trio[0]].text == "X" and board[trio[1]].text == "X" and board[trio[2]].text == "X":
                    current_move = True
        return current_move

    def step_one(self, move, board, winning_positions):
        for i in range(0, 9):
            if board[i].text == " " and move is False:
                board[i].text = self.letter
                move = self.check_if_win(board, winning_positions, move)
                if move is False:
                    board[i].text = " "

    def step_two(self, move, board, winning_positions):
        for i in range(9):
            if board[i].text == " " and move is False:
                board[i].text = "X" if self.letter == "O" else "O"
                move = self.check_if_lose(board, winning_positions, move)
                if move is False:
                    board[i].text = " "
                else:
                    board[i].text = self.letter

    def step_three(self, move, board, winning_positions):
        corners = [0, 2, 6, 8]
        for corner in corners:
            if board[corner].text == " " and move is False:
                board[corner].text = self.letter
                move = True

    def step_four(self, move, board, winning_positions):
        if board[4].text == " ":
            board[4].text = self.letter
            move = True

    def step_five(self, move, board, winning_positions):
        sides = [1, 3, 5, 7]
        for side in sides:
            if board[side].text == " " and move is False:
                board[side].text = self.letter
                move = True

    def make_ai_move(self, board, winning_positions):
        move = False
        self.step_one(move, board, winning_positions)
        if move is False:
            self.step_two(move, board, winning_positions)
        if move is False:
            self.step_three(move, board, winning_positions)
        if move is False:
            self.step_four(move, board, winning_positions)
        if move is False:
            self.step_five(move, board, winning_positions)