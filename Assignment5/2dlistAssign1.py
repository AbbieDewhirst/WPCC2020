# Abbie Dyck
# 110046150

def empty(grids):
    for i in grids:
        for val in i:
            if val != 0:
                return False
    return True


def find(grids, value):
    for i in range(len(grids)):
        if value in grids[i]:
            spot = [i, grids[i].index(value)]
            return spot
    spot = [-1, -1]
    return spot


grid = [[23, 34, 67], [44, 5, 3], [7, 8, 9]]

print(empty(grid))
print(find(grid, 67))
