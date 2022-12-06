# EPITECH, 2022
# ADVENT OF CODE
# File description:
# Day 5

from shutil import move


def oneStar(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    for i in range(0, len(content)):
        if (content[i] == '\n'):
            nb_stack = content[i-1].split('\n')[0]
            stacks = content[:i-1]
            moves = content[i+1:]

    my_stacks = []
    for i in range(0, len(nb_stack)):
        if (nb_stack[i] != ' '):
            my_stacks.append([])
            for j in range(0, len(stacks)):
                if (stacks[j][i] != ' '):
                    my_stacks[-1].append(stacks[j][i])

    for k in range(0, len(my_stacks)):
        my_stacks[k].reverse()
    for i in moves:
        i = i.split(' ')
        for j in range(0, int(i[1])):
            my_stacks[int(i[5].split('\n')[0]) - 1].append(my_stacks[int(i[3]) - 1].pop())
    result = ""
    for i in range(0, len(my_stacks)):
        result += my_stacks[i][-1]
    return(result)

def twoStars(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    for i in range(0, len(content)):
        if (content[i] == '\n'):
            nb_stack = content[i-1].split('\n')[0]
            stacks = content[:i-1]
            moves = content[i+1:]

    my_stacks = []
    for i in range(0, len(nb_stack)):
        if (nb_stack[i] != ' '):
            my_stacks.append([])
            for j in range(0, len(stacks)):
                if (stacks[j][i] != ' '):
                    my_stacks[-1].append(stacks[j][i])

    for k in range(0, len(my_stacks)):
        my_stacks[k].reverse()
    for i in moves:
        i = i.split(' ')
        for j in range(int(i[1]), 0, -1):
            my_stacks[int(i[5].split('\n')[0]) - 1].append(my_stacks[int(i[3]) - 1].pop(-j))
    result = ""
    for i in range(0, len(my_stacks)):
        result += my_stacks[i][-1]
    return(result)

#print(oneStar("Day_5/input.txt"))
print(twoStars("Day_5/input.txt"))