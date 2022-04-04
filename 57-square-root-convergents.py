import itertools
from fractions import Fraction


def main():

    x = square_root_convergents(1000)
    print(x)


def square_root_convergents(limit):
    result = 0
    f = Fraction(1, 2 + (Fraction(1, 2)))
    for i in range(2, limit + 1, 1):
        f = Fraction(1, 2 + f)
        if fraction_check(1 + f):
            result += 1

    return result


def fraction_check(fraction):
    n = str(fraction.numerator)
    d = str(fraction.denominator)
    return len(n) > len(d)


if __name__ == "__main__":
    main()
