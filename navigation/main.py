from grid_map import grid, start, goal
from astar import astar

path = astar(grid, start, goal)

for r in range(len(grid)):

    row_string = ""

    for c in range(len(grid[0])):

        if (r, c) == start:
            row_string += "R "

        elif (r, c) == goal:
            row_string += "G "

        elif (r, c) in path:
            row_string += "* "

        elif grid[r][c] == 1:
            row_string += "X "

        elif grid[r][c] == 2:
            row_string += "S "

        elif grid[r][c] == 3:
            row_string += "^ "

        else:
            row_string += ". "

    print(row_string)
print("\nPath:")

if path:
    print(path)
else:
    print("No path found")