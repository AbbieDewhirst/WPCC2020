# Abbie Dyck
# 110046150

def subtract(list1, list2):
    smallList = list2 if len(list2) < len(list1) else list1
    bigList = list1 if len(list1) > len(list2) else list2
    list3 = []

    for i in range(len(bigList)):
        if bigList[i] not in smallList:
            list3.append(bigList[i])
    return list3


print(subtract([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 6, 8]))
