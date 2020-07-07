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
        from onePlayer import OnePlayerScreen
        best_score = -math.inf
        ai_best_move = -1
        new_board = list()
        best_depth = math.inf
        best_wins = 0
        for i in range(9):
            new_board.append(board[i].text)
        for i in range(9):
            #depth = 0
            # print("hey"+str(i))
            if new_board[i] == " ":
                new_board[i] = self.letter
                score_depth = self.get_score(new_board, 0, False,  player, 0)
                score = score_depth[0]
                depth = score_depth[1]
                possible_wins = score_depth[2]
                print("move: "+str(i)+" score: "+str(score)+" depth: "+str(depth)+" wins: "+str(possible_wins))
                new_board[i] = " "
                if score > best_score:
                    best_score = score
                    best_depth = depth
                    ai_best_move = i
                elif score == best_score and depth < best_depth:
                    best_depth = depth
                    ai_best_move = i
                elif score == best_score and depth == best_depth and best_wins < possible_wins:
                    best_score = score
                    best_depth = depth
                    best_wins = possible_wins
                    ai_best_move = i
        #print("best ai move is "+str(ai_best_move))
        board[ai_best_move].text = self.letter
        print("------------------------")
        return board

    def get_score(self, new_board, depth, is_maxi, player, possible_wins):
        result = self.check_score(new_board)
        if result != "NOT DONE":
            if result == "TIE":
                # print("tie")
                return [0, depth, possible_wins]
            if result == self.letter:
                possible_wins += 1
                # print("ai wins")
                return [1, depth, possible_wins]
            if result == player:
                # print("player wins")
                return [-1, depth, possible_wins]
        if is_maxi: # If AI player
            best_score = -math.inf
            best_depth = math.inf
            best_wins = possible_wins
            for i in range(9):
                if new_board[i] == " ":
                    new_board[i] = self.letter
                    score_depth = self.get_score(new_board, depth + 1, False, player, possible_wins)
                    score = score_depth[0]
                    depth = score_depth[1]
                    possible_wins = score_depth[2]
                    new_board[i] = " "
                    if score > best_score:
                        best_score = score
                        best_depth = depth
                        # ai_best_move = i
                    elif score == best_score and depth < best_depth:
                        best_depth = depth
                        # ai_best_move = i
                    elif score == best_score and depth == best_depth and best_wins < possible_wins:
                        best_score = score
                        best_depth = depth
                        best_wins = possible_wins
            return [best_score, best_depth, best_wins]
        else:
            best_score = math.inf
            best_depth = 0
            best_wins = possible_wins
            for i in range(9):
                if new_board[i] == " ":
                    new_board[i] = player
                    score_depth = self.get_score(new_board, depth + 1, True, player, possible_wins)
                    score = score_depth[0]
                    depth = score_depth[1]
                    possible_wins = score_depth[2]
                    new_board[i] = " "
                    if score < best_score:
                        best_score = score
                        best_depth = depth
                        # ai_best_move = i
                    elif score == best_score and depth < best_depth:
                        best_depth = depth
                        #  ai_best_move = i
                    elif score == best_score and depth == best_depth and best_wins < possible_wins:
                        best_score = score
                        best_depth = depth
                        best_wins = possible_wins
            return [best_score, best_depth, best_wins]
