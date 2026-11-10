def normalise(text):
    return text.strip().replace(" ", "").replace("-", "").upper()


def is_valid(reg):
    if len(reg) not in (9, 10):
        return False

    return (reg[:2].isalpha()
            and reg[2:4].isdigit()
            and reg[4:-4].isalpha()
            and reg[-4:].isdigit()
            and len(reg[4:-4]) in (1, 2))


def format_reg(reg):
    if not is_valid(reg):
        return "Invalid registration"

    return reg[:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]


tests = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "KL 07 C 4567",
    "AP-39-XY-1234"
]

for raw in tests:
    reg = normalise(raw)
    print(raw, "->", reg, "->", format_reg(reg))
