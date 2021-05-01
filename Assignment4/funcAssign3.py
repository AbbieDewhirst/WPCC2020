# Abbie Dyck
# 110046150

def lowestCommonMultiple(num1, num2):
    if num1 > num2:
        biggerNum = num1
    else:
        biggerNum = num2
    while True:
        if (biggerNum % num1 == 0) and (biggerNum % num2 == 0):
            lcm = biggerNum
            break
        biggerNum += 1
    return lcm


print("LCM:", lowestCommonMultiple(int(7), int(5)))
