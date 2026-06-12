def exploration_score(position):
    row, col = position

    center_row = 2
    center_col = 2

    distance_from_center = (
        abs(row - center_row) +
        abs(col - center_col)
    )
    return 100 - distance_from_center
unknown_cells = [
    (0, 4),
    (1, 3),
    (2, 2),
    (3, 1),
    (4, 0),
]

def choose_target(cells):
    best = None
    best_score = -999999

    for cell in cells:

        score = exploration_score(cell)

        if score > best_score:
            best = cell
            best_score = score

    return best