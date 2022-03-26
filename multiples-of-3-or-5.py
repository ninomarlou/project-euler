def main():
    x = multiples_of_3_or_5(1000)
    print(x)


def multiples_of_3_or_5(n):

    result = sum(i for i in range(1000) if (i % 3 == 0 or i % 5 == 0))

    return result


if __name__ == "__main__":
    main()
