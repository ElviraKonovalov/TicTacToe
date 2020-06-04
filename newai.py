import math

class AiNew:

    def __init__(self, letter):
        self.letter = letter

    def make_ai_best_move(self, board, player):
        best_score = -math.inf
        ai_best_move = None
        new_board = list()
        best_depth = 0
        for i in range(9):
            new_board.append(board[i].text)
        for i in range(9):
            if new_board[i] == " ":
                new_board[i] = self.letter
                score_depth = self.get_score(new_board, best_depth, False,  player)
                score = score_depth[0]
                depth = score_depth[1]
                new_board[i] = " "
                if score == best_score and depth < best_depth:
                    best_score = score
                    best_depth = depth
                    ai_best_move = i
                if score > best_score:
                    best_score = score
                    ai_best_move = i
        board[ai_best_move].text = self.letter

    def get_score(self, board, depth, is_maxi, player):
        from onePlayer import OnePlayerScreen
        result = OnePlayerScreen.check_win
        if result != "NULL":
            if result == "TIE":
                print("tie")
                return [0, depth]
            if result == self.letter:
                print("ai wins")
                return [1, depth]
            elif result == player:
                print("player wins")
                return [-1, depth]
        if is_maxi: # If AI player
            best_score = -math.inf
            best_depth = 0
            for i in range(9):
                if board[i] == " ":
                    board[i] = self.letter
                score_depth = self.get_score(board, depth + 1, False, player)
                score = score_depth[0]
                depth = score_depth[1]
                board[i] = " "
                if score > best_score:
                    best_score = score
                    best_depth = depth
                elif score == best_score and depth < best_depth:
                    best_score = score
                    best_depth = depth
            return [best_score, best_depth]
        else:
            best_score = math.inf
            best_depth = 0
            for i in range(9):
                if board[i] == " ":
                    board[i] = player
                score_depth = self.get_score(board, depth + 1, True, player)
                score = score_depth[0]
                depth = score_depth[1]
                board[i] = " "
                if score < best_score:
                    best_score = score
                    best_depth = depth
                elif score == best_score and depth < best_depth:
                    best_score = score
                    best_depth = depth
            return [best_score, best_depth]
