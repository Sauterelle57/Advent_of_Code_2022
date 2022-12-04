# EPITECH, 2022
# ADVENT OF CODE
# File description:
# Day 4

def oneStar(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    total = 0
    for i in content:
        i = i.split('\n')[0]
        elve1, elve2 = i.split(',')
        if int(elve1.split('-')[0]) <= int(elve2.split('-')[0]) and int(elve1.split('-')[1]) >= int(elve2.split('-')[1]):
            print(elve1, ' ', elve2)
            total += 1
        elif int(elve2.split('-')[0]) <= int(elve1.split('-')[0]) and int(elve2.split('-')[1]) >= int(elve1.split('-')[1]):
            print(elve1, ' ', elve2)
            total += 1
    return(total)

def twoStars(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    total = 0
    for i in content:
        i = i.split('\n')[0]
        elve1, elve2 = i.split(',')
        if int(elve2.split('-')[0]) >= int(elve1.split('-')[0]) and int(elve2.split('-')[0]) <= int(elve1.split('-')[1]):
            total += 1
        elif int(elve1.split('-')[0]) >= int(elve2.split('-')[0]) and int(elve1.split('-')[0]) <= int(elve2.split('-')[1]):
            total += 1

    return(total)

#print(oneStar("Day_4/input.txt"))
print(twoStars("Day_4/input.txt"))