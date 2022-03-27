import sympy


def main():

    x = n_prime(10000)
    print(x)


def n_prime(n):
    prime_count = 0
    i = 0
    counter = 1
    while prime_count <= n:
        i += 1
        if sympy.isprime(i):
            prime_count += 1

    return i


if __name__ == "__main__":
    main()
