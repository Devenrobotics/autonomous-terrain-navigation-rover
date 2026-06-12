from grid_map import grid, start, goal
from mission import checkpoints
from astar import astar

current = start
full_path = [start]

for name, checkpoint in checkpoints:

    segment = astar(grid, current, checkpoint)

    if segment is None:
        print(f"Cannot reach checkpoint {name}")
        exit()

    full_path.extend(segment[1:])
    current = checkpoint

segment = astar(grid, current, goal)

if segment is None:
    print("Cannot reach goal")
    exit()

full_path.extend(segment[1:])

checkpoint_positions = {
    pos: name
    for name, pos in checkpoints
}

for r in range(len(grid)):

    row_string = ""

    for c in range(len(grid[0])):

        pos = (r, c)

        if pos == start:
            row_string += "R "

        elif pos == goal:
            row_string += "G "

        elif pos in checkpoint_positions:
            row_string += checkpoint_positions[pos] + " "

        elif pos in full_path:
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

print("\nMission route:")
print(full_path)