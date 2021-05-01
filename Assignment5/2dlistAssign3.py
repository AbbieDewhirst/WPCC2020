# Abbie Dyck
# 110046150

import math
import random


def treePlacement(treePlace):
    for i in range(10):
        treePlace.append([random.randint(0, 29), random.randint(0, 29)])
    return treePlace


def check(trees):
    for i in range(9):
        for j in range((i + 1), 10):
            treeA = trees[i]
            treeB = trees[j]
            distance = math.sqrt(((treeB[0] - treeA[0]) ** 2) + ((treeB[1] - treeA[1]) ** 2))
            if distance < 3:
                return False
    return True


treeSpots = []
tree = []

for i in range(30):
    treeSpots.append([])
    for n in range(30):
        treeSpots[i].append('_')

while True:
    tree = treePlacement(tree)
    plantSuccess = check(tree)
    if plantSuccess:
        break
    tree = []

for i in range(10):
    treeSpots[tree[i][1]][tree[i][0]] = 'X'

for i in range(30):
    for j in range(30):
        print(treeSpots[i][j], end=' ')
    print()
