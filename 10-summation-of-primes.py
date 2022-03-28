import sympy
from functools import reduce


def main():

    x = summation_of_prime(2000000)
    print(x)


def summation_of_prime(n):

    prime_range = range(2, n + 1)
    prime_range_filtered = filter(fast_prime_check, prime_range)
    result = reduce(prime_check, prime_range)
    return result


def fast_prime_check(n):
    if not (int(str(i)[-1]) in (0, 2, 4, 5, 6, 8) and i not in [2, 5]):
        if not (sum(int(x) for x in str(i)) % 3 == 0 and i != 3):
            return True
        else:
            return False
    else:
        return False


def prime_check(a, b):
    if sympy.isprime(b):
        result = a + b
    else:
        result = a
    return result


if __name__ == "__main__":
    main()
