# Abbie Dyck
# 110046150

import random

ssNames = []

while True:
    names = input("Enter name (x to generate assignments): ")
    if names == "x":
        break
    ssNames.append(names)

alreadyPicked = []
ss = []

for i in range(len(ssNames)):
    rand = ""
    while True:
        rand = random.choice(ssNames)
        if rand not in alreadyPicked and rand != ssNames[i]:
            alreadyPicked.append(rand)
            break
    ss.append("{0} gifts {1}".format(ssNames[i], rand))

random.shuffle(ss)

for i in range(len(ss)):
    print(ss[i])
