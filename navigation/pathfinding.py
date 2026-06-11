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