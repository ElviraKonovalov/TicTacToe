import math


class AiNew:

    winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal win
                         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical win
                         [0, 4, 8], [2, 4, 6]  # Diagonal win
                         ]

    def __init__(self, letter):
        self.letter = letter

    def check_score(self, new_board):
        from onePlayer import OnePlayerScreen
        for trio in self.winning_positions:
            if new_board[trio[0]] == "X" and new_board[trio[1]] == "X" and new_board[trio[2]] == "X":
                return "X"
            if new_board[trio[0]] == "O" and new_board[trio[1]] == "O" and new_board[trio[2]] == "O":
                return "O"
            if OnePlayerScreen.filledBox >= 8:
                return "TIE"
        return "NOT DONE"

    def make_ai_best_move(self, board, player):
        best_score = -math.inf
        ai_best_move = -1
        new_board = list()
        best_depth = 0
        for i in range(9):
            new_board.append(board[i].text)
        for i in range(9):
            depth = 0
            # print("hey"+str(i))
            if new_board[i] == " ":
                new_board[i] = self.letter
                score_depth = self.get_score(new_board, depth, False,  player)
                score = score_depth[0]
                depth = score_depth[1]
                print("move: "+str(i)+" score: "+str(score)+" depth: "+str(depth))
                new_board[i] = " "
                if score > best_score:
                    best_score = score
                    best_depth = depth
                    ai_best_move = i
                elif score == best_score and depth < best_depth:
                    best_depth = depth
                    ai_best_move = i
        #print("best ai move is "+str(ai_best_move))
        board[ai_best_move].text = self.letter
        print("------------------------")
        return board

    def get_score(self, new_board, depth, is_maxi, player):
        result = self.check_score(new_board)
        if result != "NOT DONE":
            if result == "TIE":
                # print("tie")
                return [0, depth]
            if result == self.letter:
                # print("ai wins")
                return [1, depth]
            if result == player:
                # print("player wins")
                return [-1, depth]
        if is_maxi: # If AI player
            best_score = -math.inf
            best_depth = 0
            for i in range(9):
                if new_board[i] == " ":
                    new_board[i] = self.letter
                    score_depth = self.get_score(new_board, depth + 1, False, player)
                    score = score_depth[0]
                    depth = score_depth[1]
                    new_board[i] = " "
                    if score > best_score:
                        best_score = score
                        best_depth = depth
                        # ai_best_move = i
                    elif score == best_score and depth < best_depth:
                        best_depth = depth
                        # ai_best_move = i
            return [best_score, best_depth]
        else:
            best_score = math.inf
            best_depth = 0
            for i in range(9):
                if new_board[i] == " ":
                    new_board[i] = player
                    score_depth = self.get_score(new_board, depth + 1, True, player)
                    score = score_depth[0]
                    depth = score_depth[1]
                    new_board[i] = " "
                    if score < best_score:
                        best_score = score
                        best_depth = depth
                        # ai_best_move = i
                    elif score == best_score and depth < best_depth:
                        best_depth = depth
                        #  ai_best_move = i
            return [best_score, best_depth]
