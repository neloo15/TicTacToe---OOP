from Model import *
from View import *
import json
import random


class Controller:
    """Processes user input and applies it to the view and/or model"""
    def __init__(self):
        self.model = Model()
        self.view = View(Model())
        self.call_function_times = 0

    def get_move(self):
        self.chosen_position = None
        while self.chosen_position not in self.model.valid_inputs:
            try:
                self.chosen_position = int(input("\nPlease, give a spot's position: "))
            except TypeError:
                quit()
            except ValueError:
                print("\nPlease, give a valid number: ")
            except KeyboardInterrupt:
                quit()
            if self.chosen_position in self.model.valid_inputs:
                break
        return self.chosen_position

    def is_empty(self, board, chosen_position):
        while board[chosen_position] != ' ':
            self.view.print_is_taken()
            chosen_position = self.get_move()
            return True
        return False

    def make_move(self, board, chosen_position, player):
        while board[chosen_position] != ' ':
            print(f"Can't make move {chosen_position}, square already taken!") # realize in print view
            chosen_position = self.get_move()
        board[chosen_position] = player

    def player(self):
        if self.model.player == 'O':
            self.model.player = 'X'
        else:
            self.model.player = 'O'
            # print O is turn
        return self.model.player

    def computer(self, board):
        bs = -1000
        for key in board.keys():
            print(f"current key is {key}")
            if (board[key] == ' '):
                board[key] = 'O'
                print(f"current score is {self.bestScore}")
                self.score = self.minimax(board, False)
                print(f"minmax score {self.score}")
                print(self.model.board)
                board[key] = ' '
                if (self.score > self.bestScore):
                    self.bestScore = self.score
                    print(f"bestsscore {self.bestScore}")
                    self.bestMove = key
                    print(f"Best move {self.bestMove}")
        return self.bestMove

    def random_move(self, board):
        r = random.choice(board)
        while True:
            if r[board] == ' ':
                return r


    def minimax(self, board, is_maximizing):
        print(f"position in calculation {self.model.board}")
        self.call_function_times = self.call_function_times + 1
        print(f"call function times {self.call_function_times}")

        if sel.model.get_winner()  == 'O':
            return 1
        elif sel.model.get_winner() == 'X':
            return -1
        elif sel.model.get_winner() == ' ':
            return 0


        if is_maximizing:
            bestScore = -99
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = 'O'
                    score = self.minimax(board, False)
                    board[key] = ' '
                    if (score > bestScore):
                        bestScore = score
            return bestScore
        else:
            bestScore = 99
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = 'X'
                    score = self.minimax(board, True)
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

    def ask_load(self):
        inp = input(self.view.want_previous_game())
        if inp == 'y':
            self.model.board = self.load_game()

    def player_mode(self):
        self.ask_load()
        self.view.print_player_mode()
        while True:
            self.view.print_board(self.model.board)
            self.save_game()
            if self.model.get_winner() != ' ':
                self.view.print_winner()
                break
            elif self.model.is_draw():
                self.view.print_draw()
                break
            if self.model.whose_move() == 'X':
                pass
            else:
                self.model.player = 'O'
            self.make_move(self.model.board, self.get_move(), self.player())

    def ai_mode(self):
        self.ask_load()
        self.view.print_ai_mode()
        counter = 0
        while True:
            self.view.print_board(self.model.board)
            # comp move
            if self.model.get_winner() != ' ':
                self.view.print_winner()
                break
            if counter % 2 == 0:
                self.make_move(self.model.board, self.get_move(), self.player())
                self.view.print_winner()
            else:
                print(f"{self.computer(self.model.board)}")
                self.make_move(self.model.board, self.computer(self.model.board), self.player())
                self.model.winner=' '
            counter += 1

    def random_move(self, board):
        while True:
            r = random.randint(1, 9)
            print(f"here is r: {r}")
            if board[r] == ' ':
                board[r] = 'O'
                break
            else:
                continue

    def random_mode(self):
        self.ask_load()
        self.view.print_ai_mode()
        counter = 0
        while True:
            self.view.print_board(self.model.board)
            if self.model.get_winner() != ' ':
                self.view.print_winner()
                break
            if counter % 2 == 0:
                self.make_move(self.model.board, self.get_move(), 'X')
                self.view.print_winner()
            else:
                self.random_move(self.model.board)
                self.model.winner=' '
            counter += 1

    def which_mode(self):
        inp = input(self.view.choose_mode())
        if inp == 'a':
            self.ai_mode()
        else:
            self.player_mode()

    def play(self):
        self.view.greet()
        try:
            self.which_mode()
        except KeyboardInterrupt:
            quit()
