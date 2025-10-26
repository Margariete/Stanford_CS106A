def do_move(grid, x1, y1, x2, y2):
    #print(grid)
    #print(grid[y1][x1])
    temp= grid[y1][x1]
    grid[y1][x1]=grid[y2][x2]
    grid[y2][x2]=temp
    #print (grid)
    return grid

    """"
    Given grid and 2 coordinates.
    Move the value that is at x1,y1 to x2,y2,
    and return the resulting grid.
    Assume that this is a legal move: all coordinates are in
    bounds, and x2,y2 is empty.
    (i.e. a different function checks that this is a
    legal move before do_move() is called)
    (Doctests provided)
    
    >>> grid = [['r', 's', 'r'], ['r', None, 'r']]
    >>> do_move(grid, 1, 0, 1, 1)
    [['r', None, 'r'], ['r', 's', 'r']]
    >>> grid = [['r', 's', 's'], [None, None, None]]
    >>> do_move(grid, 1, 0, 1, 1)
    [['r', None, 's'], [None, 's', None]]
    >>> grid = [['r', 's', 's'], [None, None, None]]
    >>> do_move(grid, 2, 0, 2, 1)
    [['r', 's', None], [None, None, 's']]
    """

def main():
    grid = [['r', 's', 'r'], ['r', None, 'r']]
    new= do_move(grid,1,0,1,1)



if __name__ == '__main__':
    main()