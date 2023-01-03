def roller(content):
    try:
        if content[6].lower() == "h" or content[6].lower() == "r":
            return "roll1"

        elif content[5]:
            return "roll2"
    except:
        return "Insert roll as either: 4d + 5 or 4n + 5 or r3t2 + 3 or h3o2 + 5"
