from grid_map import grid, start
from astar import astar
from exploration import choose_best_science_target
from battery import route_cost

target = choose_best_science_target()

path = astar(grid, start, target)

cost = route_cost(path, grid)

for r in range(len(grid)):

    row_string = ""

    for c in range(len(grid[0])):

        pos = (r, c)

        if pos == start:
            row_string += "R "

        elif pos == target:
            row_string += "T "

        elif path and pos in path:
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

print("\nChosen target:", target)
print("Battery cost:", cost)