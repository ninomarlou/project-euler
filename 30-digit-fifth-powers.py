def main():
    e = 5
    limit = 999999
    x = digit_fifth_powers(e, limit)
    print(x)


def digit_fifth_powers(e, limit):
    result = 0
    for i in range(2, limit, 1):
        if i == sum([int(x)**e for x in str(i)]):
            result += i
    return result


if __name__ == "__main__":
    main()
