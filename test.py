def getBestMove(state, player):
    '''
    Minimax Algorithm
    '''
    done = check_current_state(state)
    if done == self.letter :  # If AI won
        return 1
    elif done == "Done" and winner_loser == 'X':  # If Human won
        return -1
    elif done == "Draw":  # Draw condition
        return 0

    moves = []
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if state[i][j] is ' ':
                empty_cells.append(i * 3 + (j + 1))

    for empty_cell in empty_cells:
        move = {}
        move['index'] = empty_cell
        new_state = copy_game_state(state)
        play_move(new_state, player, empty_cell)

        if player == 'O':  # If AI
            result = getBestMove(new_state, 'X')  # make more depth tree for human
            move['score'] = result
        else:
            result = getBestMove(new_state, 'O')  # make more depth tree for AI
            move['score'] = result

        moves.append(move)

    # Find best move
    best_move = None
    if player == 'O':  # If AI player
        best = -infinity
        for move in moves:
            if move['score'] > best:
                best = move['score']
                best_move = move['index']
    else:
        best = infinity
        for move in moves:
            if move['score'] < best:
                best = move['score']
                best_move = move['index']

    return best_move


import math




class AiNew:

    def __init__(self, letter):
        self.letter = letter

    def make_ai_best_move(self, board, player):
        best_score = -math.inf
        ai_best_move = None
        new_board = list()
        best_depth = 0
        turn = self.letter
        #score = [0, 0]
        for i in range(9):
            new_board.append(board[i].text)
        for i in range(9):
            if new_board[i] == " ":
                new_board[i] = self.letter
                score_depth = self.get_score(new_board, best_depth, turn,  player)
                score = score_depth[0]
                depth = score_depth[1]
                new_board[i] = " "
                if score == best_score and depth < best_depth:
                    best_score = score
                    best_depth = depth
                    ai_best_move = i
                if score > best_score:
                    best_score = score
                    best_depth = depth
                    ai_best_move = i
        board[ai_best_move].text = self.letter

    def get_score(self, board, depth, turn, player):
        from onePlayer import OnePlayerScreen
        result = check_current_state(board)
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
        if turn == self.letter: # If AI player
            best_score = -math.inf
            best_depth = 0
            for i in range(9):
                if board[i] == " ":
                    board[i] = self.letter
                score_depth = self.get_score(board, depth + 1, turn, player)
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
                score_depth = self.get_score(board, depth + 1, turn, player)
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

 if randint(0, 1) == 1:
            self.turn = self.ai
            print("Hello Player! Computer plays first!\n"+"player: "+self.player+"\n"+"ai: "+self.ai.letter)
            self.popup_message("Hello Player! Computer plays first!\n"+"player: "+self.player+"\n"+"ai: "+self.ai.letter)
            self.board = self.ai.make_ai_best_move(self.board, self.player)
            self.turn = self.player
        else:
            self.turn = self.player
            print("Hello Player! You play first!\n"+"player: "+self.player+"\n"+"ai: "+self.ai.letter)
            self.popup_message("Hello Player! Computer plays first!\n"+"player: "+self.player+"\n"+"ai: "+self.ai.letter)