from astar import astar
from battery import route_cost
from grid_map import grid, start

unknown_cells = {
    (0, 4): 30,
    (1, 3): 15,
    (2, 2): 50,
    (3, 1): 25,
    (4, 0): 40
}


def choose_best_science_target():

    best_target = None
    best_score = -999999

    for target, science_value in unknown_cells.items():

        path = astar(grid, start, target)

        if path is None:
            continue

        battery_cost = route_cost(path, grid)

        score = science_value - battery_cost

        if score > best_score:
            best_score = score
            best_target = target

    return best_target