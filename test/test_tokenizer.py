import unittest
from fractions import Fraction

from operationsonfractions.expression_eval import tokenize_expr, InfixOperator
from operationsonfractions.mixed_number import MixedNumber


class Tokenize(unittest.TestCase):

    def test_empty_expression(self):
        exp = ''
        tokens = tokenize_expr(exp)

        self.assertEqual(tokens, [])

    def test_full_whitespace_expression(self):
        exp = '  \t   \t\r   \r\n    \n  \n  '
        tokens = tokenize_expr(exp)

        self.assertEqual(tokens, [])

    def test_whitespace_expression(self):
        exp = '\n    \t \r    \n       \n       5         \t\r       \n'
        tokens = tokenize_expr(exp)

        self.assertEqual(tokens, [5])

    def test_nill_param_raise_exception(self):
        exp = None

        self.assertRaises(Exception, lambda _: tokenize_expr(exp))

    def test_int_literal(self):
        arr_int = [x for x in range(9999)]
        exp = ' '.join([str(x) for x in arr_int])
        tokens = tokenize_expr(exp)

        self.assertEqual(tokens, arr_int)

    def test_fraction_literal(self):
        arr_fractions = [Fraction(x % 100, x) for x in range(1, 9999)]
        exp = ' '.join(['{0}/{1}'.format(x.numerator, x.denominator) for x in arr_fractions])
        tokens = tokenize_expr(exp)

        self.assertEqual(tokens, arr_fractions)

    def test_mixed_number_literal(self):
        arr_mixed_numbers = [MixedNumber(x, x % 100, x) for x in range(1, 9999)]
        exp = ' '.join(
            ['{0}_{1}/{2}'.format(x.whole, x.fraction.numerator, x.fraction.denominator) for x in arr_mixed_numbers]
        )
        tokens = tokenize_expr(exp)

        self.assertEqual(tokens, arr_mixed_numbers)

    def test_operators_literals(self):
        exp = '+-*/'
        tokens = tokenize_expr(exp)

        self.assertEqual(tokens, [
            InfixOperator('+'),
            InfixOperator('-'),
            InfixOperator('*'),
            InfixOperator('/'),
        ])

    def test_complex_expression(self):
        exp = ' 12 +34/56 * /7_8/9 -    '
        tokens = tokenize_expr(exp)

        self.assertEqual(tokens, [
            12,
            InfixOperator('+'),
            Fraction(34, 56),
            InfixOperator('*'),
            InfixOperator('/'),
            MixedNumber(7, 8, 9),
            InfixOperator('-'),
        ])

    def test_unrecognized_token(self):
        exp = '5 s'
        self.assertRaises(SyntaxError, lambda _: tokenize_expr(exp), [2])

    def test_bad_mixed_number(self):
        exp = '5_4 /4'
        self.assertRaises(SyntaxError, lambda _: tokenize_expr(exp), [1])


if __name__ == '__main__':
    unittest.main()
