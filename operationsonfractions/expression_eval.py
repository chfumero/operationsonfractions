import re
from fractions import Fraction

from .mixed_number import MixedNumber, simplify_fraction

LITERAL_MIXED = 'Mixed'
LITERAL_NUMBER = 'Number'
LITERAL_FRACTION = 'Fraction'
LITERAL_OPERATOR = 'Operator'

TOKEN_REGEX = re.compile(
    '\s*(?:(?P<{0}>\d+_\d+\/\d+)|(?P<{1}>\d+\/\d+)|(?P<{2}>\d+)|(?P<{3}>\+|\-|\*|\/))'.format(
        LITERAL_MIXED,
        LITERAL_FRACTION,
        LITERAL_NUMBER,
        LITERAL_OPERATOR
    )
)


class InfixOperator:
    def __init__(self, code):
        self.code = code
        self.priority = 1 if code in ['*', '/'] else 0

    def execute(self, a, b):
        if self.code == '+':
            return a + b
        elif self.code == '-':
            return a - b
        elif self.code == '*':
            return a * b
        elif self.code == '/':
            return a / b

        raise NotImplementedError('operation not supported')

    def __str__(self):
        return 'op[{0}]'.format(self.code)

    def __repr__(self):
        return 'op[{0}]'.format(self.code)

    def __eq__(self, other):
        if type(other) is not InfixOperator:
            return False

        return self.code == other.code


def __fraction_from_str(text):
    split = text.split('/')
    return Fraction(int(split[0]), int(split[1]))


def tokenize_expr(exprarg):
    if exprarg is None:
        raise Exception('expression None')

    tokens = []
    token_types = {
        LITERAL_MIXED: lambda match_str: MixedNumber.from_expression(match_str),
        LITERAL_NUMBER: lambda match_str: int(match_str),
        LITERAL_OPERATOR: lambda match_str: InfixOperator(match_str),
        LITERAL_FRACTION: lambda match_str: __fraction_from_str(match_str),
    }

    exprarg = exprarg.rstrip()

    last_index = 0
    match = TOKEN_REGEX.match(exprarg)
    while match:
        token = token_types[match.lastgroup](match.group(match.lastgroup))
        tokens.append(token)

        last_index = match.end()
        match = TOKEN_REGEX.match(exprarg, pos=last_index)

    if last_index != len(exprarg):
        raise SyntaxError(last_index)

    return tokens


def peek(arr):
    return arr[-1] if len(arr) else None


def expression_eval(expression):
    operators = []
    output = []

    tokens = tokenize_expr(expression)
    for token in tokens:

        if isinstance(token, MixedNumber) or isinstance(token, int) or isinstance(token, Fraction):
            output.append(token)
        elif isinstance(token, InfixOperator):
            current_operator = token

            last_operator = peek(operators)
            while last_operator and last_operator.priority >= current_operator.priority:
                operand2 = output.pop()
                operand1 = output.pop()
                operator = operators.pop()

                output.append(operator.execute(operand1, operand2))
                last_operator = peek(operators)

            operators.append(current_operator)

    while len(operators):
        operand2 = output.pop()
        operand1 = output.pop()
        operator = operators.pop()

        output.append(operator.execute(operand1, operand2))

    return simplify_fraction(output[0])
