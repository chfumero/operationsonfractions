import re

from .mixed_number import MixedNumber

LITERAL_MIXED = 'Mixed'
LITERAL_NUMBER = 'Number'

OPERATOR_PLUS = 'Plus'
OPERATOR_PROD = 'Prod'
OPERATOR_DIV = 'Div'
OPERATOR_SUB = 'Sub'

TOKEN_REGEX = re.compile(
    '(?P<{0}>\d+_\d+/\d+)|(?P<{1}>\d+)|(?P<{2}>\+)'.format(LITERAL_MIXED, LITERAL_NUMBER, OPERATOR_PLUS)
)


class InfixOperator:
    def __init__(self, priority, code):
        self.code = code
        self.priority = priority

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


def _tokenize_expr(exprarg):
    tokens = []
    token_types = {
        LITERAL_MIXED: lambda match_str: MixedNumber.from_expression(match_str),
        LITERAL_NUMBER: lambda match_str: int(match_str),
        OPERATOR_PROD: lambda match_str: InfixOperator('*', 1),
        OPERATOR_DIV: lambda match_str: InfixOperator('/', 1),
        OPERATOR_PLUS: lambda match_str: InfixOperator('+', 0),
        OPERATOR_SUB: lambda match_str: InfixOperator('-', 0),
    }

    exprarg = exprarg.replace(' ', '')

    last_index = 0
    match = TOKEN_REGEX.match(exprarg)
    while match:
        token = token_types[match.lastgroup](match.group())
        tokens.append(token)

        last_index += len(match.group())
        match = TOKEN_REGEX.match(exprarg[last_index:])

    if last_index != len(exprarg):
        raise Exception('wrong expression')  # todo: improve this

    return tokens


def expression_eval(expression):
    operators = []
    output = []

    tokens = _tokenize_expr(expression)
    for token in tokens:

        if token is MixedNumber or token is int:
            output.append(token)
        elif token is InfixOperator:
            current_operator = token
            last_operator = operators[-1]
            while last_operator.priority > current_operator.priority:
                operand2 = output.pop()
                operand1 = output.pop()
                operator = operators.pop()

                output.append(operator.execute(operand1, operand2))

    while len(operators):
        operand2 = output.pop()
        operand1 = output.pop()
        operator = operators.pop()

        output.append(operator.execute(operand1, operand2))

    return output[0]
