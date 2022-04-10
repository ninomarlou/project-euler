import sympy
from eulerlib import primes
import itertools
from collections import Counter


def main():

    x = prime_pair_sets(10000, 5)
    print(x)


def prime_pair_sets(n, set_len):
    prime_list = primes(n)
    len_prime_list = len(prime_list)
    prime_pairs = {}

    for i in range(0, len_prime_list, 1):
        counterparts = []
        for j in range(i + 1, len_prime_list, 1):
            if is_prime_pair((prime_list[i], prime_list[j])):
                counterparts.append(prime_list[j])
        if len(counterparts) > 1:
            prime_pairs[prime_list[i]] = counterparts

    results = [[digit] for digit in prime_list]

    while set_len > 1:
        temp_results = []
        for result in results:
            potential_pairs = prime_pairs.get(result[-1])
            if potential_pairs:
                for k in range(0, len(result) - 1, 1):
                    another_potential_pair = prime_pairs.get(result[k])
                    potential_pairs = list((Counter(potential_pairs) & Counter(another_potential_pair)).elements())
            if potential_pairs:
                for potential_pair in potential_pairs:
                    temp_results.append(result + [potential_pair])
        results = temp_results
        set_len -= 1

    return min([sum(digits) for digits in results])


def is_prime_pair(n_pair):
    return sympy.isprime(int(str(n_pair[0]) + str(n_pair[1]))) and sympy.isprime(int(str(n_pair[1]) + str(n_pair[0])))


if __name__ == "__main__":
    main()

