import random    # so we can place bombs randomly in grid #

# building the minesweeper function #
def minesweeper(n, b):
    grid = [['-'] * n for _ in range(n)]      # creates a square grid with length n #

    for value in range(b):                      # placing b number of bombs as '#' randomly in our grid and priting it #
        x = random.randint(0,n-1)
        y = random.randint(0, n-1)
        grid[x][y] = "#"
    for row in grid:
        print(row)


    for x in range(n):                      # This for loop replaces all '-' with 0 so we can add to them. #
        for y in range(n):
            if grid[x][y] != '#':
                grid[x][y] = 0

    for x in range(n):                      # Iterating over each row and every column in each row #
        for y in range(n):
            if grid[x][y] == '#' and x <= n-2  and grid[x+1][y] != "#":       # Each of the following if statments checks for a bomb in the position and a diffrent neiboughing position, unless the position doesn't have a neighough in that direction #
                grid[x+1][y] += 1                                                 # If the conditons are met 1 is added to the value of the neighoughing position #

            if x >= 1 and grid[x][y] == '#' and grid[x-1][y] != "#":          # This if statment for example is adding 1 to the position left of a bomb, if the bomb is on the left edge it can't do this. Which is why the x >= 1 conditon exsists. #
                grid[x-1][y] += 1

            if y <= n-2 and grid[x][y] == '#' and grid[x][y+1] != "#":
                grid[x][y+1] += 1

            if y >= 1 and grid[x][y] == '#' and grid[x][y-1] != "#":
                grid[x][y-1] += 1

            if x <= n-2 and y <= n-2 and grid[x][y] == '#' and grid[x+1][y+1] != "#":
                grid[x+1][y+1] += 1

            if x <= n-2 and y >= 1 and grid[x][y] == '#' and grid[x+1][y-1] != "#":
                grid[x+1][y-1] += 1

            if x >= 1 and y <= n-2 and grid[x][y] == '#' and grid[x-1][y+1] != "#":
                grid[x-1][y+1] += 1

            if x >= 1 and y >= 1 and grid[x][y] == '#' and grid[x-1][y-1] != "#":
                    grid[x-1][y-1] += 1
    print("\n")
    for row in grid:
        print(row)      # Each row is printed sepratly, so a grid is formed #

n = int(input("Your minefield will be square, what length would you like the sides?\n"))  # User is asked for a grid size and number of bombs #
b = int(input("How many bombs would you like to place in your minefield?\n"))
minesweeper(n, b)                                                                            # Minesweeper function is ran #
