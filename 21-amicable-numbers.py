from functools import reduce


def main():

    x = amicable_numbers(10000)
    print(x)


def amicable_numbers(n):
    result = []
    rng = [x for x in range(1, n) if x % 2 == 0]
    for digit in rng:
        a = get_proper_divisors_sum(digit)
        b = get_proper_divisors_sum(a)
        if digit == b and digit != a:
            result.append(digit)
            result.append(a)
            rng.remove(a)
    return sum(result)


def get_proper_divisors_sum(n):
    return sum([divisor for divisor in range(1, int(n / 2) + 1) if n % divisor == 0])


if __name__ == "__main__":
    main()
