from constants import X2B_MAP, B2X_MAP, UNPRINTABLE_MAP

# Base translation functions


def bin_to_dec(binary_string):
    decimal, power = 0, 1

    for bit in binary_string:
        decimal += int(bit) * power
        power *= 2

    return decimal


def bin_to_hex(binary_string):
    # This next line provides 0 to 3 leading zeroes to binary string.
    binary_string = ("0" * ((4 - len(binary_string) % 4) % 4)) + binary_string
    output = []

    for i in range(len(binary_string) // 4):
        output.append(B2X_MAP.get(binary_string[i * 4 : (i + 1) * 4], ""))

    return "".join(output)


def dec_to_bin(decimal_string):
    return f"{int(decimal_string):b}"


def dec_to_hex(decimal_string):
    return f"{int(decimal_string):x}"


def hex_to_dec(hex_string):
    return int(hex_string, base=16)


def hex_to_bin(hex_string):
    output = []

    for ch in hex_string:
        output.append(X2B_MAP.get(ch, ""))

    return "".join(output)


def hex_to_ch(hex_string, printing="d"):
    """Translates hex bytes to ASCII.

    Not truly a base translation but helpful for human understanding.
    Options for control characters: [d]ot, [v]erbose, or [s]pace.
    """

    output = []
    for chi in range(len(hex_string) // 2):
        number = 16 * hex_to_dec(hex_string[2 * chi]) + hex_to_dec(
            hex_string[2 * chi + 1]
        )
        char = chr(number)
        if not char.isprintable():
            if printing == "d":
                char = "."
            elif printing == "v":
                char = UNPRINTABLE_MAP.get(number, ".")
            elif printing == "s":
                char = " "
            else:
                raise Exception
        output.append(char)
    return "".join(output)
