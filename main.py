import argparse
from fractions import Fraction

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This program take operations on fractions as an input and produce a fractional result')
    parser.add_argument('expression', metavar='expression', type=str, help='Operation on fractions expression')

    args = parser.parse_args()

    print(Fraction(5, 4) + Fraction(5, 4))
