# Abbie Dyck
# 110046150

print("Enter two points on a line:")
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

print("Enter a point: ")
j = int(input("j: "))
k = int(input("k: "))

slope = (y2 - y1) / (x2 - x1)
b = y1 - slope * x1

if k == (slope * j + b):
    print("The point ({0},{1}) IS on the line y={2}*x+{3}".format(j, k, slope, b))
else:
    print("The point ({0},{1}) is NOT on the line y={2}*x+{3}".format(j, k, slope, b))
