from grid_map import grid, start, goal
from pathfinding import find_path

path = find_path(grid, start, goal)

for r in range(len(grid)):
	for c in range(len(grid[0])):

		if (r, c) == start:
			print("S", end=" ")

		elif (r, c) == goal:
			print("G", end=" ")

		elif (r, c) in path:
			print("*", end=" ")

		elif grid[r][c] == 1:
			print("X", end=" ")

		else:
			print(".", end=" ")

	print()