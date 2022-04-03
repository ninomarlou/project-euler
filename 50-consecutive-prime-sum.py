import sympy
from eulerlib import primes


def main():

    x = consecutive_sum_prime(100)
    print(x)


def consecutive_sum_prime(limit):
    prime_list = primes(limit)
    print(prime_list)
    result = []
    for i in range(0, len(prime_list), 1):
        running_sum = 0
        for j in range(i, len(prime_list), 1):
            running_sum += prime_list[j]
            print(prime_list[::-1][i], prime_list[j], running_sum)

    pass


if __name__ == "__main__":
    main()
