from random import choice

SET_OF_NUMBERS = [x + 1 for x in range(9)]

class board(object):
    grid_y = grid_x = [x + 1 for x in range(9)]
    
    
    def __init__(self): 
        pass


# class row(object):
#     def __init__(self):
#         pass

class cell(object):
    has_value = False
    def __init__(self):
        pass

    def has_been_assigned_value(self):
        return self.has_value
    
    def create_random_value(self):
        return 7




if __name__ == "__main__":
    INPUT = [ "" for _ in range(9)]
    print(INPUT)