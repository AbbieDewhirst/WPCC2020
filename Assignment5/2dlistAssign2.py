# Abbie Dyck
# 110046150

def collide(fallingPiece, pieceOnGround):
    for i in range(len(falling)):
        for j in range(len(falling[i])):
            if falling[i][j] == 1 and pieceOnGround[i][j] == 1:
                return True

    return False


falling = [
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

ground = [
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
   [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
   [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
   [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
   [0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
   [0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
   [0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
   [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
   [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
   [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
   [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
   [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

print(collide(falling, ground))
