# EPITECH, 2022
# ADVENT OF CODE
# File description:
# Day 6

def test(test):
    for i in range(len(test)):
        for j in range(i + 1, len(test)):
            if (test[i] == test[j]):
                return (False)
    return (True)

def oneStar(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    start = 0
    end = 4
    while (end < len(content[0])):
        to_test = content[0][start:end]
        if (test(to_test)):
            return(end)
        else:
            start += 1
            end +=1
    return(end)

def twoStars(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    start = 0
    end = 14
    while (end < len(content[0])):
        to_test = content[0][start:end]
        if (test(to_test)):
            return(end)
        else:
            start += 1
            end +=1
    return(end)

print(oneStar("Day_6/input.txt"))
print(twoStars("Day_6/input.txt"))