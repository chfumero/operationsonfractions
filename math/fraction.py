def greatest_common_divisor(a, b):
    # https://en.wikipedia.org/wiki/Euclidean_algorithm
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def least_common_denominator(self, other):
        # https://en.wikipedia.org/wiki/Least_common_multiple
        return self.denominator * other.denominator // greatest_common_divisor(self.denominator, other.denominator)

    def __mul__(self, other):
        self.denominator *= other.denominator
        self.numerator *= other.numerator

    def __rmul__(self, other):
        self.__mul__(other)

    def __divmod__(self, other):
        self.__mul__(Fraction(numerator=other.denominator, denominator=other.numerator))

    def _get_adjusted_numerator(self, lcd):
        return (lcd / self.denominator) * self.numerator

    def __add__(self, other):
        if other is not Fraction:
            raise Exception()

        lcd = self.least_common_denominator(other)
        self.numerator = self._get_adjusted_numerator(lcd) + self._get_adjusted_numerator(lcd)
        self.denominator = lcd / self.denominator

    def __radd__(self, other):
        self.__add__(other)

    def __sub__(self, other):
        self.__add__(Fraction(numerator=other.numerator * -1, denominator=other.denominator))

    def __rsub__(self, other):
        self.numerator *= -1
        self.__add__(other)
