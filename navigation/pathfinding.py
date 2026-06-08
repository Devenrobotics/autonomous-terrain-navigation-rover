from collections import deque

def find_path(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    queue = deque([(start, [start])])

    visited = set()

    while queue:

        current, path = queue.popleft()

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        row, col = current

        moves = [
            (row+1,col),
            (row-1,col),
            (row,col+1),
            (row,col-1)
        ]

        for r,c in moves:

            if (
                0 <= r < rows
                and 0 <= c < cols
                and grid[r][c] == 0
            ):
                queue.append(
                    ((r,c), path+[(r,c)])
                )

    return None
