import functools
import sympy
import numpy as np


def main():
    x = sum_non_abundant_sums(28122)
    print(x)


def sum_non_abundant_sums(n):

    abundant_sums = []

    for i in range(2, n + 1, 1):
        if is_abundant(i):
            abundant_sums.append(i)

    sum_of_abundant_sums = custom_matrix(abundant_sums)

    check_range = range(1, n + 1)
    return sum(list(set(check_range) - set(sum_of_abundant_sums)))


def is_abundant(n):
    result = 0
    for i in range(int(n / 2), 0, -1):
        if n % i == 0:
            result += i
            if result > n:
                return True
    return result > n


def is_abundant2(n):
    arr = [i for i in range(1, int(n / 2) + 1) if n % i == 0]
    return sum(arr) > n


def custom_matrix(lst):
    result = []
    second_lst = lst.copy()
    for digit in lst:
        for second_digit in second_lst:
            result.append(digit + second_digit)
        second_lst.remove(digit)
    return result


if __name__ == "__main__":
    main()
