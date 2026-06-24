from grid_map import grid, start, goal
from astar import astar
from battery import route_cost
from exploration import (
    choose_best_science_target,
    unknown_cells,
    discover_science,
    print_memory
)

known_map = [
    [0, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1]
]


def scan_surroundings(position):

    row, col = position

    directions = [
        (0, 0),
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    for dr, dc in directions:

        r = row + dr
        c = col + dc

        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            known_map[r][c] = grid[r][c]


def print_known_map():

    print("\nKnown Map:")

    for row in known_map:
        print(row)


battery = 100
current_position = start

scan_surroundings(current_position)

print("Starting Battery:", battery)
print_known_map()

while battery > 0 and len(unknown_cells) > 0:

    target = choose_best_science_target(
        grid,
        current_position
    )

    if target is None:
        break

    path = astar(grid, current_position, target)

    if path is None:
        break

    cost = route_cost(path, grid)

    if cost > battery:
        print("Not enough battery to reach target.")
        break

    battery -= cost

    current_position = target

    scan_surroundings(current_position)

    discovered_value = discover_science(target)

    print("\nTarget:", target)
    print("Discovered Science Value:", discovered_value)
    print("Battery Cost:", cost)
    print("Battery Remaining:", battery)

    print_known_map()

    unknown_cells.remove(target)

print_memory()

print("\nReturning to base...")

return_path = astar(grid, current_position, goal)

if return_path:

    return_cost = route_cost(return_path, grid)

    if return_cost <= battery:

        battery -= return_cost

        print("Returned successfully.")
        print("Battery Remaining:", battery)

    else:

        print("Not enough battery to return.")

else:

    print("No path to base.")