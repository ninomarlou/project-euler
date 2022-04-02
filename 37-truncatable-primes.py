import sympy
from eulerlib import primes


def main():
    x = truncatable_primes()
    print(x)


def truncatable_primes():
    p = primes(1000000)
    result = 0
    result_count = 0
    for prime in p:
        if trunctable_check(prime) and prime > 10:
            result += prime
            result_count += 1
            if result_count == 11:
                return result


def trunctable_check(prime):
    prime = str(prime)
    for i in range(0, len(prime), 1):
        if sympy.isprime(int(prime[i:])) == False:
            return False
        if prime[:-i] != '' and sympy.isprime(int(prime[:-i])) == False:
            return False
    return True


if __name__ == "__main__":
    main()
