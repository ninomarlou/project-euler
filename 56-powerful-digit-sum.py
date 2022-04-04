def main():

    x = powerful_digit_sum(100)
    print(x)


def powerful_digit_sum(limit):
    result = 0
    for a in range(1, limit + 1, 1):
        for b in range(1, limit + 1, 1):
            digital_sum = calculate_digital_sum(a**b)
            if digital_sum > result:
                result = digital_sum

    return result


def calculate_digital_sum(n):
    return sum([int(digit) for digit in str(n)])


if __name__ == "__main__":
    main()
