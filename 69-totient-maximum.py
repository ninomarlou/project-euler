import math
import itertools
import sympy


def main():

    x = calculate_totient_seive(10)
    print(x)


def totient_maximum(limit):
    max_result = 0
    result = None
    for i in itertools.count(start=2):
        j = calculate_totient(i)
        #print(i, j)
        if j > max_result:
            max_result = j
            result = i
        if i == limit:
            return result


def calculate_totient(n):
    phi = 0
    limit = n - 1
    print(n, limit)
    for i in itertools.count(start=1):
        if math.gcd(n, i) == 1:
            phi += 1
        if i == limit:
            return n / phi
        if i > limit:
            return 0


def calculate_totient_seive(n):
    phi = 0
    limit = n - 1
    print(n, limit)
    for i in itertools.count(start=1):
        if math.gcd(n, i) == 1:
            print(i, 'y')
            phi += 1
        else:
            print(i, 'n')
        if i == limit:
            return n / phi
        if i > limit:
            return 0


if __name__ == '__main__':
    main()
