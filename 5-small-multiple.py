import sympy


def main():

    x = small_multiple(1, 21)
    print(x)


def small_multiple(min_n, max_n):

    # Find LCM using the division method

    cake = list(range(min_n, max_n))
    primes = list(p for p in range(min_n, max(cake)) if sympy.isprime(p))
    lcm = []
    forward = 1
    while forward:
        for prime in primes:
            prime_forward = 1
            while prime_forward:
                temp_cake = cake.copy()
                even_counter = 0
                for i in range(0, len(cake), 1):
                    if temp_cake[i] % prime == 0:
                        temp_cake[i] = int(temp_cake[i] / prime)
                        even_counter += 1
                if even_counter == 0:
                    prime_forward = 0
                else:
                    cake = temp_cake
                    lcm.append(prime)
        if sum(cake) == len(cake):
            forward = 0

    result = 1
    for digit in lcm + cake:
        result *= digit
    return result


if __name__ == "__main__":
    main()
