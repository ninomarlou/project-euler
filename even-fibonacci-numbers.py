def main():

    x = even_fibonacci_numbers(4000000)
    print(x)


def even_fibonacci_numbers(n):

    n1 = 1
    n2 = 2
    result = 0

    while n2 < n:

        if n2 % 2 == 0:
            result += n2

        n1, n2 = n2, n1 + n2

    return result


if __name__ == "__main__":
    main()
