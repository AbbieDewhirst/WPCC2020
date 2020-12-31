# Abbie Dyck
# 110046150

inputs = []
maxNums = []
num = input("Please enter marks (Enter -1 to calculate): ")
avgSum = 0
average = 0

while True:
    inputs.append(num)
    num = input()
    if num == "-1":
        break

for i in range(0, 6):
    maxNum = 0
    for j in range(len(inputs)):
        if int(inputs[j]) > int(maxNum):
            maxNum = inputs[j]
    inputs.remove(maxNum)
    avgSum += int(maxNum)
    maxNums.append(maxNum)

maxLen = len(maxNums)

if maxLen % 2 == 0:
    median1 = maxNums[maxLen//2]
    median2 = maxNums[maxLen//2-1]
    median = (int(median1) + int(median2))/2
else:
    median = maxNums[maxLen//2]


average = avgSum/6
print("Average of top 6: ", average)
print("Median of top 6: ", median)
