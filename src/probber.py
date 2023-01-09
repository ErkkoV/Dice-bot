import re

from roller import roll_gen


def prob_comparison(defence, def_skill, attack, att_skill):
    result_dict = {}

    if attack:
        i = 0
        while True:
            for key1 in defence:
                for key2 in attack:
                    if int(key1) + def_skill >= int(key2) + att_skill + i:
                        try:
                            result_dict[i] += int(defence[key1]) * int(attack[key2])
                        except:
                            result_dict[i] = int(defence[key1]) * int(attack[key2])
                    if i > 0 and int(key1) + def_skill >= int(key2) + att_skill - i:
                        try:
                            result_dict[-i] += int(defence[key1]) * int(attack[key2])
                        except:
                            result_dict[-i] = int(defence[key1]) * int(attack[key2])
            if i > 25:
                break

            i += 5
    else:
        i = 0
        while True:
            for key1 in defence:
                if int(key1) + def_skill >= att_skill + i:
                    try:
                        result_dict[i] += int(defence[key1])
                    except:
                        result_dict[i] = int(defence[key1])
                elif i > 0 and int(key1) + def_skill >= att_skill - i:
                    try:
                        result_dict[-i] += int(defence[key1])
                    except:
                        result_dict[-i] = int(defence[key1])
            i += 5
            if i > 25:
                break

    if attack:
        for key in result_dict:
            result_dict[key] = result_dict[key] / (10000 * 100)
    else:
        for key in result_dict:
            result_dict[key] = result_dict[key] / 100

    return result_dict


def prob_calc(dice, take):
    results = {}
    for x in range(10000):
        res = roll_gen(dice, take)[1]
        try:
            results[res] += 1
        except:
            results[res] = 1
    return results


def probber(content):

    try:
        if "vs" in content:
            contents = content.split("vs")
            print(contents[0], contents[1])

            if "l" in contents[1]:
                numbers = [int(s) for s in re.findall(r"\d+", contents[1])]
                attack = prob_calc(-numbers[0], 1)
                attack_skill = numbers[1]
            elif ("[") in contents[1]:
                attack = False
                attack_skill = int(content.split("[")[1].split("]")[0])
            else:
                numbers = [int(s) for s in re.findall(r"\d+", contents[1])]
                attack = prob_calc(numbers[0], numbers[1])
                attack_skill = numbers[2]

            if "l" in contents[0]:
                numbers = [int(s) for s in re.findall(r"\d+", contents[0])]
                defence = prob_calc(-numbers[0], 1)
                defence_skill = numbers[1]
            else:
                numbers = [int(s) for s in re.findall(r"\d+", contents[0])]
                defence = prob_calc(numbers[0], numbers[1])
                defence_skill = numbers[2]

            res = prob_comparison(defence, defence_skill, attack, attack_skill)

            print(res[0])

            defence_sentence = f"\nDefender Success change: {res[0]}%\nDefender Failure change: {round(100 - res[0], 2)}%\n"
            attack_sentence = f"\nAttacker Success change: {100 - res[0]}%\nAttacker Failure change: {round(res[0], 2)}%\n"

            for key in res:
                if int(key) > 0:
                    defence_sentence = (
                        f"\nDefender Crit Success {abs(int(key/5))} change: {round(res[key], 2)}%"
                        + defence_sentence
                    )
                    attack_sentence += f"Attacker Crit Failure {abs(int(key/5))} change: {round(res[key], 2)}%\n"

                elif int(key) < 0:
                    defence_sentence += f"Defender Crit Failure {abs(int(key/5))} change: {round(100 - res[key], 2)}%\n"
                    attack_sentence = (
                        f"\nAttacker Crit Success {abs(int(key/5))} change: {round(100 - res[key], 2)}%"
                        + attack_sentence
                    )

            if not attack:
                attack_sentence = ""

            return defence_sentence + attack_sentence

        else:
            print("else")
            if "l" in content:
                numbers = [int(s) for s in re.findall(r"\d+", content)]
                res = prob_calc(-numbers[0], 1)
            else:
                numbers = [int(s) for s in re.findall(r"\d+", content)]
                print(numbers)
                res = prob_calc(numbers[0], numbers[1])

            res_sentence = "Prob Array:\n"
            for each in sorted(res.keys(), reverse=True):
                res_sentence += f"{each}: {round(res[each]/100, 2)}% \n"

            return res_sentence

    except:
        return """Type probability as `/prob r3t2`\nOr type `/help prob` for correct syntax"""
