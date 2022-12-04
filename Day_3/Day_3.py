# EPITECH, 2022
# ADVENT OF CODE
# File description:
# Day 3

def oneStar(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    total = 0
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in content:
        i = i.split('\n')[0]
        present = []
        for j in range(0, round(len(i) / 2)):
            present.append(i[j])
        for k in range(round(len(i) / 2), len(i)):
            if i[k] in present:
                total += alpha.index(i[k]) + 1
                break
    return(total)

def twoStars(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    total = 0
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    items_by_group = [0 for i in range(52)]
    number = 1
    member_number = 0
    for i in content:
        i = i.split('\n')[0]
        if (member_number % 3 == 0 and member_number != 0):
            total += items_by_group.index(111) + 1
            member_number = 0
            number = 1
            items_by_group = [0 for i in range(52)]
        for j in i:
            items_by_group[alpha.index(j)] += number if items_by_group[alpha.index(j)] < number else 0
        number *= 10
        member_number += 1

    return(total + items_by_group.index(111) + 1)

print(oneStar('Day_3/input.txt'))
print(twoStars('Day_3/input.txt'))