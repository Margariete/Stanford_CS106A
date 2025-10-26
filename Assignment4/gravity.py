def main():
    grid = [[None, 's', 'r'], [None, None, None]]
    gravity = do_gravity(grid,1,0)
    print(gravity)



def do_gravity(grid,x,y):

    if grid[y][x] != 's':
        print('the dot is not sand')
        pass


    #check if we can go down
    elif grid[y+1][x] == None:
        x1=x
        y1=y
        x2=x
        y2=y+1
        checked = check_move(grid,x1,y1,x2,y2)
        if checked == True:
            new = do_move((grid,x1,y1,x2,y2)

    #check if we can go down left
    elif grid[y+1][x-1] == None:
        x1 = x
        y1 = y
        x2 = x - 1
        y2 = y + 1
        checked = check_move(grid, x1, y1, x2, y2)
        if checked == True:
            new = do_move((grid, x1, y1, x2, y2)

    #check if we can go down right
    else grid[y + 1][x + 1] == None:
        x1 = x
        y1 = y
        x2 = x + 1
        y2 = y + 1
        checked = check_move(grid, x1, y1, x2, y2)
        if checked == True:
            new = do_move((grid, x1, y1, x2, y2)

    return new




def check_move(grid, x1, y1, x2, y2):
    # check if the new coordinate is within bounds
    # print(grid)
    # print(grid[y1][x1])
    # print out the position left or right of the initial position
    # print(grid[0][2])
    rows = (len(grid))
    columns = (len(grid[0]))

        if x2 > columns - 1 or x2 < 0:
            print("x2 = " + str(x2) + " is out of bounds.")
            pass
            value = False

        elif y2 > rows - 1 or y2 < 0:
            print("y2 = " + str(y2) + " is out of bounds.")
            value = False


        # check if the new location has a None

        elif grid[y2][x2] != None:
            value = False

            # check if there is an overhange/corner rule
            #    elif x2 == x1 - 1 and y2 == y1 + 1 and grid[y1][x1 - 1] != None:
        elif x2 == x1 - 1 or x2 == x1 + 1:
            if grid[y1][x2 - 1] != None:
                value = False
                print("oh no overhange")
            else:
                value = True

        else:
            value = True

    return value




def do_move(grid, x1, y1, x2, y2):

    temp= grid[y1][x1]
    grid[y1][x1]=grid[y2][x2]
    grid[y2][x2]=temp

    return grid




if __name__ == '__main__':
    main()