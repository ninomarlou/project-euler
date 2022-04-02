import sympy
from eulerlib import primes


def main():

    x = circular_primes(1000000)
    print(x)


def circular_primes(limit):
    result = 0
    for prime_number in primes(limit):
        result += get_rotation_primes(prime_number)
    return result


def get_rotation_primes(n):

    result = 1

    str_n = list(str(n))
    digits = str_n + [''] * (7 - len(str_n))

    for i in range(0, len(str_n), 1):

        d0 = (7 + i) % 7
        d1 = (7 + i + 1) % 7
        d2 = (7 + i + 2) % 7
        d3 = (7 + i + 3) % 7
        d4 = (7 + i + 4) % 7
        d5 = (7 + i + 5) % 7
        d6 = (7 + i + 6) % 7

        if sympy.isprime(int(''.join((digits[d0] + digits[d1] + digits[d2] +
                                      digits[d3] + digits[d4] + digits[d5] + digits[d6])))) == False:
            result = 0

    return result


if __name__ == "__main__":
    main()
