# EPITECH, 2022
# ADVENT OF CODE
# File description:
# Day 2

def oneStar(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    total = 0
    value = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    for i in content:
        total += value[i[2]]
        if (value[i[0]] == value[i[2]]):
            total += 3
        if (value[i[0]] + 1 == value[i[2]]):
            total += 6
        if (value[i[0]] + 1 == value[i[2]] * 4):
            total += 6
    return(total)

def twoStars(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    total = 0
    value = {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}
    for i in content:
        total += value[i[2]]
        if (value[i[2]] == 3):
            total += value[i[0]]
        if (value[i[2]] == 6):
            total += (value[i[0]] + 1) if (value[i[0]] + 1 != 4) else 1
        if (value[i[2]] == 0):
            total += (value[i[0]] - 1) if (value[i[0]] - 1 != 0) else 3
    return(total)

#print(oneStar("Day_2/input.txt"))
print(twoStars("Day_2/test.txt"))