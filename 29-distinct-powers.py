def main():
    x = distinct_powers(2, 100)
    print(x)


def distinct_powers(a, b):

    integer_combinations = []

    for i in range(a, b + 1, 1):
        for j in range(a, b + 1, 1):
            integer_combinations.append(i ** j)

    return len(list(dict.fromkeys(integer_combinations)))


if __name__ == "__main__":
    main()
