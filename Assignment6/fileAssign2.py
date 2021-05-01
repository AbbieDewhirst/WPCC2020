# Abbie Dyck
# 110046150
file = open('people.txt', 'r')
listOfPeople = file.read()
listOfPeople = listOfPeople.strip().split("\n")

people = []
hobbies = {}

for i in range(len(listOfPeople)):
    people.append(listOfPeople[i].split(","))

for i in range(len(people)):
    for j in range(1, 4):
        if people[i][j] not in hobbies:
            hobbies[people[i][j]] = []

for i in hobbies:
    for j in range(len(people)):
        if i in people[j][1:]:
            hobbies[i].append(people[j][0] + "\n")

for i in hobbies:
    hobbyFile = open((i + '.txt'), 'x')
    hobbyFile.writelines(hobbies[i])

hobbyFile.close()
file.close()
