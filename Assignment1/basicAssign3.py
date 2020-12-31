# Abbie Dyck
# 110046150

import random

guessNum = int(input())
randomNum = random.randint(1, 9)
if guessNum == randomNum:
    print("Correct!")
else:
    print("Incorrect. The correct number was ", randomNum)
