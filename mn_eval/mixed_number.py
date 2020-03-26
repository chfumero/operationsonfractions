import re
import math
from fractions import Fraction


def simplify_fraction(fraction):
    if fraction.denominator == 1:
        return fraction.numerator

    if fraction.numerator > fraction.denominator:
        return MixedNumber(whole=math.fabs(fraction.numerator // fraction.denominator),
                           numerator=fraction.numerator % fraction.denominator,
                           denominator=fraction.denominator)

    return Fraction(numerator=fraction.numerator, denominator=fraction.denominator)


class MixedNumber:
    __MIXED_NUMBER_REGEX = re.compile('\d+_\d+/\d+')

    def __init__(self, whole, numerator, denominator):
        self.fraction = Fraction(numerator=numerator, denominator=denominator)
        self.whole = whole

    @staticmethod
    def from_expression(exp):
        match = re.match('(\d+)_(\d+)/(\d+)', exp)

        if not match:
            raise Exception('the expression doesn\'t describe a mixed number')

        return MixedNumber(int(match.group(0)), int(match.group(1)), int(match.group(2)))

    def to_improper_fraction(self):
        return Fraction(numerator=self.whole * self.fraction.denominator + self.fraction.numerator,
                        denominator=self.fraction.numerator)

    def __add__(self, other):
        improper_fraction = self.to_improper_fraction()
        out_fraction = None

        if other is int or other is Fraction:
            out_fraction = improper_fraction + other

        if other is MixedNumber:
            out_fraction = improper_fraction + other.to_improper_fraction()

        if out_fraction.denominator == 1:
            return out_fraction.numerator

        if out_fraction.numerator > out_fraction.denominator:
            return MixedNumber(whole=math.fabs(out_fraction.numerator // out_fraction.denominator),
                               numerator=out_fraction.numerator % out_fraction.denominator,
                               denominator=out_fraction.denominator)

        return out_fraction

    def __mul__(self, other):
        out_fraction = None

        if other is int or other is Fraction:
            out_fraction = self.to_improper_fraction() * other

        if other is MixedNumber:
            out_fraction = self.to_improper_fraction() * other.to_improper_fraction()

        return simplify_fraction(out_fraction)

    def __divmod__(self, other):
        out_fraction = None

        if other is int or other is Fraction:
            out_fraction = self.to_improper_fraction() / other

        if other is MixedNumber:
            out_fraction = self.to_improper_fraction() / other.to_improper_fraction()

        return simplify_fraction(out_fraction)

    def __rdivmod__(self, other):
        out_fraction = None

        if other is int or other is Fraction:
            out_fraction = other / self.to_improper_fraction()

        if other is MixedNumber:
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
        return self.whole + '_' + self.fraction.numerator + '/' + self.fraction.denominator
