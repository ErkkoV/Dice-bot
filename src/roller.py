import random
import re


def roll_gen(dice, take):
    result = 0
    list = []
    for x in range(abs(dice)):
        list.append(int(random.randint(1, 10)))
    list.sort(reverse=True)

    if dice > 0:
        allOnes = True

        for each in range(len(list)):
            if list[each] == 10:
                list[each] = 15
                allOnes = False
            elif list[each] != 1:
                allOnes = False

        if allOnes:
            result = len(list) - 5
        else:
            for x in range(take):
                result += list[x]

    else:
        for each in list:
            if each == 1:
                result -= 5

        result += list[-1]

    return [list, result]


def roller(content):
    try:
        numbers = [int(s) for s in re.findall(r"\d+", content)]

        if (
            content[6].lower() == "h"
            or content[6].lower() == "r"
            or content[6].lower() == "l"
        ):
            if content[6].lower() == "l":
                roll = -numbers[0]
                take = 1
                skill = numbers[1]
            else:
                roll = numbers[0]
                take = numbers[1]
                skill = numbers[2]

        elif content[5]:
            roll = int(numbers[0] / 2 + 1)
            if numbers[0] % 2:
                take = roll
            else:
                take = roll - 1

            if content[6] == "-" or numbers[0] < 1:
                roll = -(numbers[0] + 2)
                take = 1

            skill = numbers[1]

        res = roll_gen(roll, take)

        if "+" not in content:
            skill = -skill

        result = f"Rolled: {res[0]}, Taken: {take} Skill: {skill} **Result: {res[1] + skill}**"
        return result

    except:
        return "Insert roll as either: 4d + 5 or 4n + 5 or -4n + 5 or r3t2 + 3 or h3o2 + 5 or l4 + 5"
