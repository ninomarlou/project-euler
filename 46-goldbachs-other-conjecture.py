import itertools
import sympy


def main():
    x = goldbachs_other_conjecture()
    print(x)


def goldbachs_other_conjecture():
    for i in itertools.count(start=3, step=2):
        if perform_check(i) == False:
            return i


def perform_check(n):
    for y in range(n):
        x = (-2 * (y**2)) + n
        if x < 0:
            return False
        if sympy.isprime(x):
            return True
    return False


if __name__ == '__main__':
    main()
