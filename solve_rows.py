from random import choice
import numpy as np
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--board_size", type=int, required=False, default=3)
    return parser.parse_args()


class Board(object):
    def __init__(self, board_size) -> None:
        self.BOARD_SIZE = board_size
        self.CHOICES = [str(i+1) for i in range(self.BOARD_SIZE)]
        self.board = np.full((self.BOARD_SIZE, self.BOARD_SIZE), "")
    
    def show(self) -> None:
        print(self.board)

    def choices(self, row) -> str:
        row_set = self.row_as_set(row)
        return choice( list(set(self.CHOICES) -  row_set) ) 
        
    def row_as_set(self, row) -> set: 
        return set(row)

    def fill_row(self, row_index) -> None:
        for ix, el in enumerate(self.board[row_index]):
            # print(ix, el)
            self.board[row_index][ix] = self.choices(self.board[row_index])
        return
    
    def solve_board(self) -> None:
        for i in range(self.BOARD_SIZE):
            self.fill_row(i)

if __name__ == "__main__":
    args = get_args()
    b  = Board(args.board_size)
    b.solve_board()

    b.show()
    