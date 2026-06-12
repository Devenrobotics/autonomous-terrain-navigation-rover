terrain_energy = {
    0: 1,
    2: 5,
    3: 20
}


def route_cost(path, grid):

    if path is None:
        return None

    total_cost = 0

    for row, col in path:

        terrain = grid[row][col]

        total_cost += terrain_energy.get(terrain, 1)

    return total_cost