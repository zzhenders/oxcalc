from functions import dec_to_bin, dec_to_hex
from functions import hex_to_bin, hex_to_dec, hex_to_ch


class Stack(object):
    """A stack for RPN."""

    def __init__(self):
        self.stack = list()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) <= 0:
            raise Exception("Empty stack!")
        else:
            return self.stack.pop()

    def top(self, n):
        """Return top `n` items in stack, with top as 0th item."""

        if n < len(self.stack):
            return self.stack[::-1]
        else:
            return self.stack[-1 : (-1 * n) : -1]

    def to_number(self, str_number):
        if str_number[0] == "x":
            return int(hex_to_dec(str_number[1:]))
        if str_number[0] == "b":
            return int(bin_to_dec(str_number[1:]))

    def binary_args(self):
        return (self.to_number(self.pop()), self.to_number(self.pop()))

    def unary_arg(self):
        return self.to_number(self.pop())

    def parse(self, in_string, base):
        items = in_string.split(" ").reverse()

        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a // b,
            "%": lambda a, b: a % b,
            "&": lambda a, b: a & b,
            "|": lambda a, b: a | b,
            "^": lambda a, b: a ^ b,
            "~": lambda a: ~a,
            "<": lambda a, b: a << b,
            ">": lambda a, b: a >> b,
        }

        for item in items:
            if item in "+-*/%&|^><":
                self.push(operators[item](self.binary_args()))
            elif item in "~":
                self.push(operators[item](self.unary_arg()))
            else:
                self.stack.push(item)
