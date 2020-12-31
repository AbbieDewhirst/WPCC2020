# Abbie Dyck
# 110046150

inputMonth = int(input("Month: "))
inputDay = int(input("Day: "))

daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayInYear = sum(daysInMonths[:(inputMonth-1)]) + inputDay

print("That's day {} of the year".format(dayInYear))
