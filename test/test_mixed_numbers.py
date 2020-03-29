import unittest
from fractions import Fraction

from operationsonfractions.mixed_number import MixedNumber


class MixedNumberAddition(unittest.TestCase):

    def test_int_add_zero(self):
        self.assertEqual(MixedNumber(1, 1, 2), MixedNumber(1, 1, 2) + 0)

    def test_int_add_x(self):
        self.assertEqual(MixedNumber(5, 2, 3), MixedNumber(1, 2, 3) + 4)

    def test_int_add_x_neg(self):
        self.assertEqual(MixedNumber(3, 2, 3), MixedNumber(4, 2, 3) + -1)

    def test_int_add_x_doub_neg(self):
        self.assertEqual(MixedNumber(5, -2, 3), MixedNumber(4, -2, 3) + -1)

    def test_int_add_commutative(self):
        self.assertEqual(MixedNumber(1, 1, 2) + 5, 5 + MixedNumber(1, 1, 2))

    def test_frac_add_zero(self):
        self.assertEqual(MixedNumber(1, 1, 2), MixedNumber(1, 1, 2) + Fraction(0, 1))

    def test_frac_add_x(self):
        self.assertEqual(MixedNumber(2, 1, 6), MixedNumber(1, 1, 2) + Fraction(2, 3))

    def test_frac_add_x_neg(self):
        self.assertEqual(MixedNumber(1, 1, 10), MixedNumber(1, 1, 2) + Fraction(-2, 5))

    def test_frac_add_x_doub_neg(self):
        self.assertEqual(MixedNumber(2, -1, 6), MixedNumber(1, -1, 2) + Fraction(-2, 3))

    def test_frac_add_x_out_int(self):
        self.assertEqual(2, MixedNumber(1, 1, 2) + Fraction(1, 2))

    def test_mix_add_x(self):
        self.assertEqual(MixedNumber(4, 2, 3), MixedNumber(1, 1, 3) + MixedNumber(3, 1, 3))

    def test_mix_add_x_out_int(self):
        self.assertEqual(3, MixedNumber(1, 1, 2) + MixedNumber(1, 1, 2))

    def test_mix_add_x_neg(self):
        self.assertEqual(Fraction(-1, 6), MixedNumber(1, 1, 2) + MixedNumber(1, -2, 3))

    def test_mix_add_x_doub_neg(self):
        self.assertEqual(MixedNumber(4, -2, 3), MixedNumber(1, -1, 3) + MixedNumber(3, -1, 3))


class MixedNumberMultiplication(unittest.TestCase):

    def test_int_mul_zero(self):
        self.assertEqual(0, MixedNumber(1, 2, 3) * 0)

    def test_int_mul_identity(self):
        self.assertEqual(MixedNumber(1, 2, 3), MixedNumber(1, 2, 3) * 1)

    def test_int_mul_x(self):
        self.assertEqual(MixedNumber(17, 1, 2), MixedNumber(2, 1, 2) * 7)

    def test_int_mul_x_neg(self):
        self.assertEqual(MixedNumber(17, -1, 2), MixedNumber(2, 1, 2) * -7)

    def test_int_mul_x_doub_neg(self):
        self.assertEqual(MixedNumber(17, 1, 2), MixedNumber(2, -1, 2) * -7)

    def test_int_mul_commutive(self):
        self.assertEqual(MixedNumber(4, 1, 2) * 2, 2 * MixedNumber(4, 1, 2))

    def test_frac_mul_zero(self):
        self.assertEqual(0, MixedNumber(1, 2, 3) * Fraction(0, 1))

    def test_frac_mul_identity(self):
        self.assertEqual(MixedNumber(1, 2, 3), MixedNumber(1, 2, 3) * Fraction(1, 1))

    def test_frac_mul_x(self):
        self.assertEqual(MixedNumber(4, 3, 4), MixedNumber(9, 1, 2) * Fraction(1, 2))

    def test_frac_mul_x_neg(self):
        self.assertEqual(MixedNumber(4, -3, 4), MixedNumber(9, 1, 2) * Fraction(-1, 2))

    def test_frac_mul_x_doub_neg(self):
        self.assertEqual(MixedNumber(4, 3, 4), MixedNumber(9, -1, 2) * Fraction(-1, 2))

    def test_frac_mul_commutative(self):
        self.assertEqual(MixedNumber(1, 1, 2) * MixedNumber(1, 1, 3), MixedNumber(1, 1, 3) * MixedNumber(1, 1, 2))

    def test_mix_mul_x(self):
        self.assertEqual(MixedNumber(1, 7, 8), MixedNumber(1, 1, 2) * MixedNumber(1, 1, 4))

    def test_mix_mul_x_neg(self):
        self.assertEqual(MixedNumber(1, -7, 8), MixedNumber(1, 1, 2) * MixedNumber(1, -1, 4))

    def test_mix_mul_x_doub_neg(self):
        self.assertEqual(MixedNumber(1, 7, 8), MixedNumber(1, -1, 2) * MixedNumber(1, -1, 4))


class MixedNumberSubstraction(unittest.TestCase):
    def test_int_sub_zero(self):
        self.assertEqual(MixedNumber(2, 1, 4), MixedNumber(2, 1, 4) - 0)

    def test_int_sub_zero_reverse(self):
        self.assertEqual(MixedNumber(2, -1, 4), 0 - MixedNumber(2, 1, 4))

    def test_int_sub_x_neg(self):
        self.assertEqual(MixedNumber(4, 1, 3), MixedNumber(1, 2, 3) - MixedNumber(2, -2, 3))

    def test_frac_sub_x_out(self):
        self.assertEqual(MixedNumber(1, 1, 3), MixedNumber(1, 2, 3) - Fraction(1, 3))

    def test_frac_sub_x_out_int(self):
        self.assertEqual(1, MixedNumber(1, 2, 3) - Fraction(2, 3))

    def test_frac_sub_x_out_frac(self):
        self.assertEqual(Fraction(-2, 3), MixedNumber(1, 2, 3) - Fraction(7, 3))

    def test_mix_sub_x_out_zero(self):
        self.assertEqual(0, MixedNumber(2, 2, 3) - MixedNumber(2, 2, 3))

    def test_mix_sub_x_double_neg(self):
        self.assertEqual(1, MixedNumber(1, -2, 3) - MixedNumber(2, -2, 3))

    def test_mix_sub_x_out_frac(self):
        self.assertEqual(Fraction(1, 3), MixedNumber(2, 2, 3) - MixedNumber(2, 1, 3))

    def test_mix_sub_x_out_int(self):
        self.assertEqual(1, MixedNumber(2, 1, 2) - MixedNumber(1, 1, 2))


class MixedNumberDivision(unittest.TestCase):
    def test_int_div_zero(self):
        self.assertRaises(Exception, lambda _: MixedNumber(1, 2, 3) / 0)

    def test_int_div_identity(self):
        self.assertEqual(MixedNumber(1, 2, 3), MixedNumber(1, 2, 3) / 1)

    def test_int_div_x(self):
        self.assertEqual(MixedNumber(1, 1, 6), MixedNumber(2, 1, 3) / 2)

    def test_int_div_x_neg(self):
        self.assertEqual(MixedNumber(1, -1, 6), MixedNumber(2, 1, 3) / -2)

    def test_int_div_x_doub_neg(self):
        self.assertEqual(MixedNumber(1, 1, 6), MixedNumber(2, -1, 3) / -2)

    def test_frac_div_x(self):
        self.assertEqual(MixedNumber(3, 1, 3), MixedNumber(1, 2, 3) / Fraction(1 / 2))

    def test_mix_div_out_identity(self):
        self.assertEqual(1, MixedNumber(1, 1, 2) / MixedNumber(1, 1, 2))

    def test_mix_div_x(self):
        self.assertEqual(MixedNumber(1, 2, 3), MixedNumber(2, 1, 2) / MixedNumber(1, 1, 2))

    def test_mix_div_x_neg(self):
        self.assertEqual(MixedNumber(1, -2, 3), MixedNumber(2, 1, 2) / MixedNumber(1, -1, 2))

    def test_mix_div_x_doub_neg(self):
        self.assertEqual(MixedNumber(1, 2, 3), MixedNumber(2, -1, 2) / MixedNumber(1, -1, 2))


if __name__ == '__main__':
    unittest.main()
