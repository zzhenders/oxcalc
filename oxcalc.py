from argparse import ArgumentParser, RawDescriptionHelpFormatter
from stack import Stack

parser = ArgumentParser(
    formatter_class=RawDescriptionHelpFormatter,
    usage="""oxcalc [-h] [-b BASE] <expression>""",
    description="""Simple command-line programmer's calculator.""",
    epilog="""
bases:
  he[x]adecimal, [d]ecimal, [b]inary, [c]haracters

arithmetic operators:
  a b +
  a b -
  a b *
  a b /   integer division
  a b %   a modulo b
        
logical operators:
  a b &   and
  a b |   or
  a ~     not
  a b ^   xor
  a b <   bitshift a left by b
  a b >   bitshift a right by b

note: you may need to escape operators to avoid shell conflicts.
  """
)

parser.add_argument(
    "-b", "--base",
    help="set output base [default: x]",
    default="x",
    action="store",
    dest="base",
)

parser.add_argument("expression", action="store", help="RPN expression", nargs="*")

args = parser.parse_args()

rpn_stack = Stack()
answer = rpn_stack.parse(args.expression, args.base)
print(answer)
