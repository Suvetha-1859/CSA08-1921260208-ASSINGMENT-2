def normalise(text):
    text = text.replace(" ", "")
    text = text.replace("-", "")
    text = text.upper()
    return text


def is_valid(reg):
    if len(reg) == 9:
        return (reg[:2].isalpha() and
                reg[2:4].isdigit() and
                reg[4:5].isalpha() and
                reg[5:].isdigit())

    elif len(reg) == 10:
        return (reg[:2].isalpha() and
                reg[2:4].isdigit() and
                reg[4:6].isalpha() and
                reg[6:].isdigit())

    else:
        return False


def format_number(reg):
    if is_valid(reg):
        if len(reg) == 9:
            return reg[:2] + " " + reg[2:4] + " " + reg[4:5] + " " + reg[5:]
        else:
            return reg[:2] + " " + reg[2:4] + " " + reg[4:6] + " " + reg[6:]
    else:
        return "INVALID"


numbers = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "KL 07 C 4567",
    "AP-39-CD-5678"
]

for raw in numbers:
    reg = normalise(raw)

    if is_valid(reg):
        print(raw, "->", reg, "Valid")
        print("Receipt:", format_number(reg))
    else:
        print(raw, "->", reg, "INVALID")
