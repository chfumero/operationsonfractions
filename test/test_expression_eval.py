import unittest
from fractions import Fraction

from operationsonfractions.expression_eval import expression_eval
from operationsonfractions.mixed_number import MixedNumber


class ExpressionEval(unittest.TestCase):
    def test_nill_expression(self):
        self.assertRaises(Exception, lambda _: expression_eval(None))

    def test_empty_expression(self):
        self.assertRaises(Exception, lambda _: expression_eval(' '))

    def test_single_expressions_int(self):
        self.assertEqual(4, expression_eval('4'))

    def test_single_expressions_frac(self):
        self.assertEqual(Fraction(2, 3), expression_eval('2/3'))

    def test_single_expressions_improper_frac(self):
        self.assertEqual(MixedNumber(2, 1, 3), expression_eval('7/3'))

    def test_single_expr_mix(self):
        self.assertEqual(MixedNumber(2, 3, 4), expression_eval('2_3/4'))

    def test_simple_sum(self):
        self.assertEqual(2, expression_eval('1/2 + 1/2 + 1 - 1 + 1'))

    def test_simple_sub(self):
        self.assertEqual(-1, expression_eval('1/2 + 1/2 - 1 - 1'))

    def test_complex_exp_out_int(self):
        self.assertEqual(4, expression_eval('1/2 * 2 + 2_1/2 + 1/2 / 1'))
        self.assertEqual(4, expression_eval('1 + 1 - 1 * 1 + 1 * 1 / 1 + 2'))

    def test_simple_exp_out_mix(self):
        self.assertEqual(MixedNumber(1, 7, 8), expression_eval('1/2 * 3_3/4'))
        self.assertEqual(MixedNumber(3, 1, 2), expression_eval('2_3/8 + 9/8'))

    def test_complex_exp_out_mix(self):
        self.assertEqual(MixedNumber(5, 5, 6), expression_eval('1/3 + 1_1/2 * 2 + 1_2/3 / 2/3'))

    def test_complex_exp_out_frac(self):
        self.assertEqual(Fraction(5, 6), expression_eval('1/3 + 1_1/2 * 2 + 1_2/3 / 2/3 - 5'))

    def test_semanthic_error(self):
        self.assertRaises(Exception, lambda _: expression_eval('1/3 + + 1/3'))

    def test_parsing_error(self):
        self.assertRaises(Exception, lambda _: expression_eval('1/3 + s 1/3'))


if __name__ == '__main__':
    unittest.main()
