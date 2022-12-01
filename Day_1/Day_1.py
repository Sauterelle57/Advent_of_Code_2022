# EPITECH, 2022
# ADVENT OF CODE
# File description:
# Day 1

def oneStar(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    list_Elves_calories = [0]
    index = 0
    for i in content:
        if (i == "\n"):
            index += 1
            list_Elves_calories.append(0)
        else:
            list_Elves_calories[index] += int(i.split('\n')[0])
    return(max(list_Elves_calories))

def twoStars(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    list_Elves_calories = [0]
    index = 0
    for i in content:
        if (i == "\n"):
            index += 1
            list_Elves_calories.append(0)
        else:
            list_Elves_calories[index] += int(i.split('\n')[0])
    total = 0
    for i in range(0, 3):
        total += max(list_Elves_calories)
        list_Elves_calories.remove(max(list_Elves_calories))
    return(total)

print(oneStar("./Day_1/input.txt"))
print(twoStars("./Day_1/input.txt"))
