from Model import *
from View import *
import json

class Controller:
    """Processes user input and applies it to the view and/or model"""

    def __init__(self):
        self.model = Model()
        self.view = View(Model())



    def get_move(self):
        self.chosen_position = None
        while self.chosen_position not in self.model.valid_inputs:
            try:
                self.chosen_position = input("Please give a legal position: ")
            except KeyboardInterrupt:
                pass
            try:
                self.chosen_position = int(self.chosen_position)
            except KeyboardInterrupt:
                pass
            except ValueError:
                self.chosen_position = input("Please give a legal position: ")
            except KeyboardInterrupt:
                pass
            if self.chosen_position in self.model.valid_inputs:

                break
        return self.chosen_position

    def is_empty(self, board, chosen_position):
        while board[chosen_position] != " ":
            self.view.print_is_taken()
            chosen_position = self.get_move()
            return True
        return False


    def make_move(self, board, chosen_position, player):
        while board[chosen_position] != " ":
            print(f"Can't make move {chosen_position}, square already taken!")
            chosen_position = self.get_move()
        board[chosen_position] = player



    def player(self):
        if self.model.player == 'O':
            self.model.player = 'X'
        else:
            self.model.player = 'O'
            # print O is turn
        return self.model.player


    def computer():
        board = self.model.board
        bestScore = -1000
        bestMove = 0
        score = None
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = 'O'
                score = self.minimax(False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
                    bestMove = key
        return bestMove

    def best_move(self, computer):
        board = self.model.board
        board[computer] = 'O'

    def minimax(self, isMaximizing):
        board = self.model.board
        score = None
        if self.model.get_winner() == 'O':
            score = 1
            return score
        elif self.model.get_winner() == 'X':
            score = -1
            return score
        elif self.model.is_draw():
            score = 0
            return score
        if isMaximizing:
            bestScore = -99
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = 'O'
                    score = self.minimax(False)
                    board[key] = ' '
                    if (score > bestScore):
                        bestScore = score
            return bestScore
        else:
            bestScore = 99
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = 'X'
                    score = self.minimax(True)
                    board[key] = ' '
                    if (score < bestScore):
                        bestScore = score
            return bestScore

    def save_game(self):
        filename = 'board.json'
        data ={
            "board": self.model.board
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_game(self):
        board = None
        filename = 'board.json'
        with open(filename) as f:
            data = json.load(f)
            board = data["board"]
            board = {int(k):str(v) for k,v in board.items()}
        return board


    def player_mode(self):
        inp = input("Do you want load the previous game? y/n: ")
        if inp == 'y':
            self.model.board = self.load_game()
        while True:
            self.view.print_board(self.model.board)
            self.save_game()
            if self.model.get_winner() is not None:
                print(self.model.get_winner())
                break
            elif self.model.is_draw():
                self.view.print_draw()
                break
            self.make_move(self.model.board, self.get_move(), self.player())


    def ai_mode(self):
        counter = 0
        while True:
            self.view.print_board(self.model.board)
            if self.model.get_winner() is not None:
                print(self.model.get_winner())
                break
            if counter % 2 == 0:
                self.make_move(self.model.board, self.get_move(), self.player())
            else:
                self.make_move(self.model.board, self.computer(), self.player())
            counter += 1









