from decimal import *


def main():
    x = reciprocal_cycles(1000)
    print(x)


def reciprocal_cycles(n):
    getcontext().prec = n * 2
    result = 0
    max_reciprocity = 0
    for i in range(2, n, 1):
        reciprocal = str(Decimal(1) / Decimal(i)).split(".")[1]
        reciprocity = recurence_check_helper(reciprocal)
        if reciprocity > max_reciprocity:
            max_reciprocity = reciprocity
            result = i
    return result


def recurence_check_helper(n):
    result = -1
    for i in range(0, 3, 1):
        recurrence_count = recurence_check(n[i:])
        if recurrence_count > result:
            result = recurrence_count
    return result


def recurence_check(n):
    for i in range(1, int((len(n) + 1) / 2) + 1, 1):
        if n[:i] == n[i:i + i]:
            return i
    return -1


if __name__ == "__main__":
    main()
