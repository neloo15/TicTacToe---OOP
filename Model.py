class Model:
    def __init__(self):
        self.board = self.new_board()
        self.winner = ' '
        self.valid_inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player = 'O'

    def new_board(self):
        board = {
            1 : 'O', 2 : ' ', 3 : ' ',
            4 : ' ', 5 : ' ', 6 : ' ',
            7 : ' ', 8 : ' ', 9 : ' '
        }
        return board

    def get_winner(self):
        # Rows
        if self.board[1] == self.board[2] == self.board[3] and self.board[1] != ' ':
            self.winner = self.board[1]
        elif self.board[4] == self.board[5] == self.board[6] and self.board[4] != ' ':
            self.winner = self.board[4]
        elif self.board[7] == self.board[8] == self.board[9] and self.board[7] != ' ':
            self.winner = self.board[7]

        # Columns
        elif self.board[1] == self.board[4] == self.board[7] and self.board[1] != ' ':
            self.winner = self.board[1]
        elif self.board[2] == self.board[5] == self.board[8] and self.board[2] != ' ':
            self.winner = self.board[2]
        elif self.board[3] == self.board[6] == self.board[9] and self.board[3] != ' ':
            self.winner = self.board[3]

        # Diagonals
        elif self.board[1] == self.board[5] == self.board[9] and self.board[1] != ' ':
            self.winner = self.board[5]
        elif self.board[3] == self.board[5] == self.board[7] and self.board[3]!= ' ':
            self.winner = self.board[5]
        return self.winner

    def is_draw(self):
        for key in self.board.keys():
            if self.board[key] == ' ':
                return False
        return True

    def winner_is_found(self):
        if self.get_winner() != ' ':
            return True

    def whose_move(self):
        if sum(value == 0 for value in self.board.values()) % 2 == 0:
            return True #X is turn
        else:
            return False

    @staticmethod
    def get_winner2(board):
        winner = ' '
        # Rows
        if board[1] == board[2] == board[3] and board[1] != " ":
            winner = board[1]
        elif board[4] == board[5] == board[6] and board[4] != " ":
            winner = board[4]
        elif board[7] == board[8] == board[9] and board[7] != " ":
            winner = board[7]

        # Columns
        elif board[1] == board[4] == board[7] and board[1] != " ":
            winner = board[1]
        elif board[2] == board[5] == board[8] and board[2] != " ":
            winner = board[2]
        elif board[3] == board[6] == board[9] and board[3] != " ":
            winner = board[3]

        # Diagonals
        elif board[1] == board[5] == board[9] and board[1] != " ":
            winner = board[5]
        elif board[3] == board[5] == board[7] and board[3] != " ":
            winner = board[5]
        return winner