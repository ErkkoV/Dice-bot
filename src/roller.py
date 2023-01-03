import re


def roller(content):
    try:
        numbers = [int(s) for s in re.findall(r"\d+", content)]
        print(numbers)

        if content[6].lower() == "h" or content[6].lower() == "r" or content[6].lower() == "l":
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

        result = f"{roll}, {take}, {skill}"
        return result

    except:
        return "Insert roll as either: 4d + 5 or 4n + 5 or -4n + 5 or r3t2 + 3 or h3o2 + 5 or l4 + 5"
