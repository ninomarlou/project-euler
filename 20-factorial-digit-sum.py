def main():

    x = factorial_digit_sum(100)
    print(x)


def factorial_digit_sum(n):
    factorial = 1
    for i in range(1, n + 1, 1):
        factorial *= i
    return sum([int(d) for d in str(factorial)])


if __name__ == "__main__":
    main()
