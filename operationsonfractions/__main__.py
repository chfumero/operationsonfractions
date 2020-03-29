import argparse
from .expression_eval import expression_eval


def main():
    parser = argparse.ArgumentParser(
        description='This program take operations on fractions as an input and produce a fractional result'
    )
    parser.add_argument('expression', metavar='expression', type=str, help='Operation on fractions expression')

    args = parser.parse_args()

    try:
        print(str(expression_eval(args.expression)))
    except SyntaxError as e:
        print('char {}: Syntax error close to "{}"'.format(e.args[0], args.expression[e.args[0]:]))
    except:
        print('Something went wrong, please review your expression')


if __name__ == "__main__":
    main()
