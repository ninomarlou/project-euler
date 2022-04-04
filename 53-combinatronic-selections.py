import math


def main():

    x = combinatronic_selections(100)
    print(x)


def combinatronic_selections(limit):
    result = 0
    for n in range(1, limit + 1, 1):
        for r in range(1, n + 1, 1):
            if calculate(n, r) > 1000000:
                result += 1
    return result


def calculate(n, r):
    return math.factorial(n) / ((math.factorial(r)) * (math.factorial(n - r)))


if __name__ == "__main__":
    main()
