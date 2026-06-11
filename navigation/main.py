from grid_map import grid, start, goal
from pathfinding import find_path

path = find_path(grid, start, goal)

print("Path found:")
print(path)