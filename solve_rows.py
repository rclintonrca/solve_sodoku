from random import choice, sample
import numpy as np


class Board(object):
    def __init__(self, board_size=9) -> None:
        self.board_size = board_size
        self.choices = [str(i+1) for i in range(self.board_size)]
        self.board = np.full((self.board_size, self.board_size), "")
    
    def show(self) -> None:
        print(self.board)

    def chosen_number(self, row) -> str:
        row_set = self.row_as_set(row)
        return choice( list(set(self.choices) -  row_set) ) 
        
    def row_as_set(self, row) -> set: 
        return set(row)

    def fill_row(self, row_index) -> None:
        for ix, el in enumerate(self.board[row_index]):
            if el == '':
                self.board[row_index][ix] = self.chosen_number(self.board[row_index])
            else:
                continue
        return
    
    def make_board_one(self) -> None:
        self.board[0][0] = '0'
        self.board[1][1] = '1'
        self.board[2][2] = '2'
        return

    def solve_board(self) -> None:
        for i in range(self.board_size):
            self.fill_row(i)

if __name__ == "__main__":
    # args = get_args()
    b  = Board()
    b.make_board_one()
    b.show()
    print()

    b.solve_board()

    b.show()

    """
    steps
    1. random choice
    2. if number hits constraint; try again
        3. if no number fits (we should find this out first); go back one cell and change it
        4. continue forward 1-3
    5. either move forward, or move backward and change cell again (so we do need state to know all the values?)
    """
    