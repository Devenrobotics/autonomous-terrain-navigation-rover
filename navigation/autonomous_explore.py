from grid_map import grid, start, goal
from astar import astar
from battery import route_cost
from exploration import choose_best_science_target, unknown_cells

battery = 100
current_position = start

print("Starting Battery:", battery)

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

    science_value = unknown_cells[target]

    print("\nTarget:", target)
    print("Science Value:", science_value)
    print("Battery Cost:", cost)
    print("Battery Remaining:", battery)

    current_position = target

    del unknown_cells[target]

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