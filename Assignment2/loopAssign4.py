# Abbie Dyck
# 110046150

num = 1
sumOfNum = 0
counter = 0
largest = None
smallest = None


while num != 0:
    num = int(input(""))
    sumOfNum += num
    if num == 0:
        break
    if largest is None:
        largest = num
    if num > largest:
        largest = num
    if smallest is None:
        smallest = num
    if num < smallest:
        smallest = num
    counter += 1

average = sumOfNum/counter
print("Average: ", average, "\nLargest: ", largest, "\nSmallest:", smallest)
