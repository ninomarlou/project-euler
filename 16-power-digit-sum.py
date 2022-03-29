def main():

    x = power_digit_sum(1000)
    print(x)


def power_digit_sum(e):
    digits = [int(d) for d in str(2**e)]
    return sum(digits)


if __name__ == "__main__":
    main()
