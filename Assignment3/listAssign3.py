# Abbie Dyck
# 110046150

from random import randint

generatedBirthdays = []
counter = 0

while True:
    birthday = randint(1, 365)
    if birthday in generatedBirthdays:
        break
    generatedBirthdays.append(birthday)
    counter += 1

print("Birthdays generated before duplicate:", counter)
