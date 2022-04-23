
def main():
    x = powerful_digit_counts(10)


def powerful_digit_counts(n):
    np = 1
    for i in range(n):
        print(np)
        np = np * 10


if __name__ == '__main__':
    main()
