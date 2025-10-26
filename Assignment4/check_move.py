

def main():
    grid = [[None, 's', 'r'], [None, None, None]]
    checked = check_move(grid, 1, 0, 2, 1)


def check_move(grid, x1, y1, x2, y2):
    #check if the new coordinate is within bounds
    #print(grid)
    #print(grid[y1][x1])
    #print out the position left or right of the initial position
    #print(grid[0][2])
    rows=(len(grid))
    columns=(len(grid[0]))

    if x2 > columns-1 or x2 < 0:
        print("x2 = " + str(x2) + " is out of bounds.")
        value = False

    elif y2 > rows-1 or y2 < 0:
        print("y2 = " + str(y2)+ " is out of bounds.")
        value = False


    #check if the new location has a None

    elif grid[y2][x2] != None:
        value = False

    #check if there is an overhange/corner rule
    #    elif x2 == x1 - 1 and y2 == y1 + 1 and grid[y1][x1 - 1] != None:
    elif x2 == x1 - 1 or x2 == x1 +1:
        if grid[y1][x2-1] != None:
            value = False
            print("oh no overhange")
        else:
            value = True

    else:
        value = True

    return value

"""
    Given grid, starting point (x1,y1) and destination (x2,y2).
    Check if it's possible to move the value at (x1,y1) to (x2,y2).
    The (x1,y1) location is always in bounds of the grid, but (x2,y2)
    may not be.
    Return True if the move is okay, or False otherwise.
    Okay move: (x2,y2) in bounds, empty, and not violating corner rule.
    
    
    
    >>> # Provided out-of-bounds tests
    >>> grid = [[None, 's', 'r'], [None, None, None]]
    >>> check_move(grid, 0, 0, -1, 0) # x2 = -1 is out of bounds
    False
    >>> check_move(grid, 0, 0, 0, 4)  # y2 = 4 is out of bounds
    False
    >>> check_move(grid, 0, 0, 3, 1)  # x2 = 3 is out of bounds
    False
    >>> # Provided empty destination checks
    >>> check_move(grid, 1, 0, 0, 0)  # left ok
    True
    >>> check_move(grid, 1, 0, 2, 0)  # right blocked
    False
    >>> check_move(grid, 1, 0, 1, 1)  # down, ok
    True
    >>> # Provided corner rule checks
    >>> # check down-left move from (1,0)
    >>> check_move(grid, 1, 0, 0, 1)  # down-left ok, corner rule
    True
    >>> # check down-right move from (1,0)
    >>> check_move(grid, 1, 0, 2, 1)  # down-right blocked, corner rule
    False
    """


if __name__ == '__main__':
    main()