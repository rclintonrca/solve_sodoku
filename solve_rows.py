from random import choice, sample
import numpy as np

class StuckException(Exception):
    """
    Raised when an invalid CMBS Type is specified
    """

class Board(object):
    def __init__(self, board_size=9) -> None:
        self.board_size = board_size
        self.choices = [str(i+1) for i in range(self.board_size)]
        self.board = np.full((self.board_size, self.board_size), "")
        self.set_of_choices = set(self.choices)
    
    def show(self) -> None:
        print(self.board)

    def chosen_number(self, row) -> str:
        row_set = self.row_as_set(row)
        return choice( list(set(self.choices) -  row_set) ) 
        
    def column_from_ix(self, ix):
        return self.board.transpose()[ix]
    
    def chosen_number_v2(self, row_set, column_set) -> str:
        used_values: set = row_set | column_set
        possible_choices = list(self.set_of_choices -  used_values)
        
        if len(possible_choices) > 0:
            return choice(possible_choices)
        else:
            raise StuckException

    def fill_cell(self, row_index, ix)->None:  
            set_of_column_values = set(self.column_from_ix(ix))
            set_of_row_values = set(self.board[row_index])
            
            try:
                answer = self.chosen_number_v2(set_of_row_values, set_of_column_values)
                self.board[row_index][ix] = answer
                self.show()

            except StuckException:
                print(f"HELP... I am stuck at...\n\t COL: {row_index} \n\t ROW: {ix}")
                self.show()
                print()
                # as a blunt approach i will replace the prior cell with an empty string and then try again...
                #  the correct thing to do now is to try and do the ix-1 cell now
                self.board[row_index][ix - 1 ] = '' 
                self.fill_cell(row_index, ix - 1 )
                # reset cell to left
                # keep track of what values previous cell was so only new values are tried
                # TODO: need to step back more than one time if it does not work
                pass

    def fill_row(self, row_index) -> None:
        for ix, el in enumerate(self.board[row_index]):
            if el == '':
                self.fill_cell(row_index, ix)
            else:
                continue
        return
    
    def make_board_one(self) -> None:
        self.board[0][0] = '1'
        self.board[0][1] = '2'
        self.board[1][1] = '1'
        self.board[2][2] = '2'
        return

    def solve_board(self) -> None:
        for i in range(self.board_size):
            self.fill_row(i)

if __name__ == "__main__":
    # args = get_args()
    b  = Board(3)
    b.make_board_one()
    b.show()
    # print(b.board.transpose())
    # print()
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
    