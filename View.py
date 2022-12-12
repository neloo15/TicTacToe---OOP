from Model import *

class View:
    """View is just for printing states and highlights input hints"""
    def __init__(self, model):
        self.model = model

    def print_board(self, board):
        print('Current board:')
        print('+---+---+---+')
        print(f"| {board[1]} | {board[2]} | {board[3]} |   1  2  3")
        print('+---+---+---+')
        print(f"| {board[4]} | {board[5]} | {board[6]} |   4  5  6")
        print('+---+---+---+')
        print(f"| {board[7]} | {board[8]} | {board[9]} |   7  8  9")
        print('+---+---+---+')

    def print_winner(self):
        print(self.model.get_winner())

    def print_draw(self):
        print("No winner - it's a draw!")

    def print_is_taken(self):
        print("That square already taken!")

    def momo(self):
        return "selfoooo"


