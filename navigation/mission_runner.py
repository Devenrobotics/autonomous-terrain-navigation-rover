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

print("Mission route:")
print(full_path)