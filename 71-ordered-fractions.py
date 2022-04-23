import math
from fractions import Fraction
from eulerlib import primes


def main():

    x = x_ordered_fractions(8)
    print(x)


def ordered_fractions(n):
    pass


def x_ordered_fractions(d_limit):

    relative_primes = []
    prime_list = primes(d_limit + 1)
    none_prime_list = list(set(list(range(2, d_limit + 1))) - set(prime_list))
    print(prime_list)
    print(none_prime_list)

    # prime numbers
    for p in prime_list:
        relative_primes += [(n, p) for n in list(range(1, p))]

    for p in none_prime_list:
        relative_primes += [(n, p) for n in primes(p - 1)]

    relative_primes_fractions = [Fraction(x[0], x[1]) for x in relative_primes]

    for p in sorted(relative_primes_fractions):
        print(p)


if __name__ == '__main__':
    main()
