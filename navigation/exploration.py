from astar import astar
from battery import route_cost

# Unexplored locations
unknown_cells = {
    (0, 4),
    (1, 3),
    (2, 2),
    (3, 1),
    (4, 0)
}

# Hidden science values
science_map = {
    (0, 4): 10,
    (1, 3): 20,
    (2, 2): 30,
    (3, 1): 40,
    (4, 0): 5
}

# What the rover has learned so far
rover_memory = {}


def discover_science(target):
    """
    Discover and store the science value
    of a location after visiting it.
    """

    value = science_map[target]

    rover_memory[target] = value

    return value


def print_memory():
    """
    Display everything the rover has learned.
    """

    print("\nRover Memory:")

    if len(rover_memory) == 0:
        print("No discoveries yet.")
        return

    for location, value in rover_memory.items():
        print(f"Location: {location}, Science Value: {value}")


def get_area_interest(target):
    """
    Calculate how interesting an area is
    based on nearby discoveries.
    """

    total_interest = 0

    for location, value in rover_memory.items():

        distance = (
            abs(location[0] - target[0])
            + abs(location[1] - target[1])
        )

        if distance <= 2:
            total_interest += value

    return total_interest


def choose_best_science_target(grid, current_position):
    """
    Choose the next target based on:
    - learned interest from nearby discoveries
    - battery cost to reach the target
    """

    best_target = None
    best_score = -999999

    for target in unknown_cells:

        path = astar(grid, current_position, target)

        if path is None:
            continue

        battery_cost = route_cost(path, grid)

        interest = get_area_interest(target)

        score = interest - battery_cost

        if score > best_score:

            best_score = score
            best_target = target

    return best_target