from functions import dec_to_bin, dec_to_hex
from functions import hex_to_bin, hex_to_dec, hex_to_ch


class Stack(object):
    """A stack for RPN."""

    def __init__(self):
        self.stack = list()

    def push(data):
        self.stack.append(data)

    def pop():
        if len(self.stack) <= 0:
            raise Exception("Empty stack!")
        else:
            return self.stack.pop()

    def parse(in_string):
        items = in_string.split(" ").reverse()

        for item in items:
            if item in "+-*/%&|~^><":
                pass
            else:
                pass
