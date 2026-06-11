import heapq

terrain_cost = {
    0: 1,   # normal terrain
    2: 100,   # sand
    3: 1000   # steep slope
}

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}

    g_score = {start: 0}

    while open_set:

        _, current = heapq.heappop(open_set)

        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path

        row, col = current

        neighbors = [
            (row+1, col),
            (row-1, col),
            (row, col+1),
            (row, col-1)
        ]

        for r, c in neighbors:

            if not (0 <= r < rows and 0 <= c < cols):
                continue

            if grid[r][c] == 1:
                continue

            terrain = grid[r][c]
            cost = terrain_cost.get(terrain, 1)

            tentative_g = g_score[current] + cost

            neighbor = (r, c)

            if (
                neighbor not in g_score
                or tentative_g < g_score[neighbor]
            ):

                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                f_score = (
                    tentative_g
                    + heuristic(neighbor, goal)
                )

                heapq.heappush(
                    open_set,
                    (f_score, neighbor)
                )

    return None