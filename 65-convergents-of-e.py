
from fractions import Fraction
import functools
import operator


def main():
    x = convergents_of_e(10)


def convergents_of_e(n):

    for i in range(1, n + 1, 1):
        e = Fraction(1, (1 + Fraction(1, i))**i)
        print(e)


def factorial(n):
    rng = range(1, n + 1)
    result = functools.reduce(operator.mul, rng)
    return result


if __name__ == '__main__':
    main()
