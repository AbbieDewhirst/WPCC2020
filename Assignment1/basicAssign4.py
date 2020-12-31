# Abbie Dyck
# 110046150

number = int(input())
answer = 0
originalNum = number

while number > 0:
    remainder = number % 10
    answer = answer + remainder
    number = int(number/10)

print(answer)
