import re
import math
from fractions import Fraction


def simplify_fraction(fraction):
    if type(fraction) is not Fraction:
        return fraction

    if fraction.denominator == 1:
        return fraction.numerator

    if abs(fraction.numerator) > fraction.denominator:
        return MixedNumber(whole=int(abs(fraction.numerator) // fraction.denominator),
                           numerator=(abs(fraction.numerator) % fraction.denominator) *
                                     (-1 if fraction.numerator < 0 else 1),
                           denominator=fraction.denominator)

    return Fraction(numerator=fraction.numerator, denominator=fraction.denominator)


class MixedNumber:
    __MIXED_NUMBER_REGEX = re.compile('\d+_\d+/\d+')

    def __init__(self, whole, numerator, denominator):
        self.fraction = Fraction(numerator=int(numerator), denominator=int(denominator))
        self.whole = int(whole)

    @staticmethod
    def from_expression(exp):
        match = re.match('(\d+)_(\d+)/(\d+)', exp)

        if not match:
            raise Exception('the expression doesn\'t describe a mixed number')

        return MixedNumber(int(match.group(1)), int(match.group(2)), int(match.group(3)))

    def to_improper_fraction(self):
        numerador = int((self.whole * self.fraction.denominator + abs(self.fraction.numerator)) *
                        (-1 if self.fraction.numerator < 0 else 1))
        return Fraction(
            numerator=numerador,
            denominator=self.fraction.denominator)

    def __add__(self, other):
        other_type = type(other)

        improper_fraction = self.to_improper_fraction()
        out_fraction = None

        if other_type is int or other_type is Fraction:
            out_fraction = improper_fraction + other

        if other_type is MixedNumber:
            out_fraction = improper_fraction + other.to_improper_fraction()

        if out_fraction.denominator == 1:
            return out_fraction.numerator

        if out_fraction.numerator > out_fraction.denominator:
            return MixedNumber(whole=math.fabs(out_fraction.numerator // out_fraction.denominator),
                               numerator=out_fraction.numerator % out_fraction.denominator,
                               denominator=out_fraction.denominator)

        return simplify_fraction(out_fraction)

    def __mul__(self, other):
        other_type = type(other)

        out_fraction = None

        if other_type is int or other_type is Fraction:
            out_fraction = self.to_improper_fraction() * other

        if other_type is MixedNumber:
            out_fraction = self.to_improper_fraction() * other.to_improper_fraction()

        return simplify_fraction(out_fraction)

    def __truediv__(self, other):
        other_type = type(other)
        out_fraction = None

        if other_type is int or other_type is Fraction:
            out_fraction = self.to_improper_fraction() / other

        if other_type is MixedNumber:
            out_fraction = self.to_improper_fraction() / other.to_improper_fraction()

        return simplify_fraction(out_fraction)

    def __rtruediv__(self, other):
        other_type = type(other)
        out_fraction = None

        if other_type is int or other_type is Fraction:
            out_fraction = other / self.to_improper_fraction()

        if other_type is MixedNumber:
            out_fraction = other.to_improper_fraction() / self.to_improper_fraction()

        return simplify_fraction(out_fraction)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-1 * other)

    def __rsub__(self, other):
        return other + (self.__mul__(-1))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return '{}_{}/{}'.format(int(self.whole), self.fraction.numerator, self.fraction.denominator)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if type(other) is not MixedNumber:
            return False
        return self.whole == other.whole and self.fraction.__eq__(other.fraction)
