import sympy
import math
from eulerlib import primes


def main():
    x = truncatable_primes()
    print(x)


def truncatable_primes():
    p = primes(1000000)
    result = []
    for prime in p:
        if trunctable_check(prime) and prime > 10:
            result.append(prime)
        if len(result) == 11:
            return sum(result)


def trunctable_check(prime):
    result = True
    prime = str(prime)
    for i in range(0, len(prime), 1):
        if sympy.isprime(int(prime[i:])) == False:
            result = False
        if prime[:-i] != '' and sympy.isprime(int(prime[:-i])) == False:
            result = False
        # print(prime[i:], prime[:-i], prime[:-i] == '')
    return result


if __name__ == "__main__":
    main()
