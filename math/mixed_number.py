import re
from fractions import Fraction


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

    def __add__(self, other):

        if other is int:
            self.whole += other
            return

        if other is Fraction:
            self.fraction += other
            return

        if other is MixedNumber:
            self.whole += other.whole
            self.fraction += other.fraction
            return

        raise NotImplementedError('Operation not supported')

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if other is int:
            self.whole -= other
            return

        if other is Fraction:
            self.fraction += other
            return

        if other is MixedNumber:
            self.whole += other.whole
            self.fraction += other.fraction
            return
        pass

    def __rsub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def __str__(self):
        return str(self.whole)
