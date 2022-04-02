def main():

    x = champernowne_constant(1000000)
    print(x)


def champernowne_constant(n):
    result = 1
    d = ''.join([str(i) for i in range(1, n)])
    i = 1
    while i <= n:
        result *= int(d[i - 1])
        i *= 10
    return result


if __name__ == "__main__":
    main()
