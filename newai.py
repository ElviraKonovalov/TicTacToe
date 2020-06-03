import math


class AiNew:

    def __init__(self, letter):
        self.letter = letter

    def make_ai_best_move(self, board):
        best_score = -math.inf
        ai_best_move = -1
        new_board = list()
        for i in range(9):
            new_board.append(board[i].text)
        for i in range(9):
            if new_board[i] == " ":
                new_board[i] = self.letter
                score = self.get_score(new_board, 0)
                new_board[i] = " "
                if score > best_score:
                    best_score = score
                    ai_best_move = i
        board[ai_best_move].text = self.letter

    def get_score(self, board, depth):
        from onePlayer import OnePlayerScreen
        result = OnePlayerScreen.check_win
        if result != " ":
            if result == "TIE":
                print("tie")
                return 0
            if result == self.letter:
                print("ai wins")
                return 1
            else:
                print("player wins")
                return -1
        best_score = -math.inf
        for i in range(9):
            if board[i].text == " ":
                board[i].text = self.letter
                score = self.get_score(board, depth+1)
                best_score = max(score, best_score)
        return best_score

