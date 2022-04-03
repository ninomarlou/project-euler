import itertools


def main():
    x = self_powers(1000)
    print(x)


def self_powers(n):
    digits = [digit**digit for digit in range(1, n + 1)]
    result = itertools.accumulate(digits)
    return str(list(result)[-1])[-10:]


if __name__ == '__main__':
    main()
