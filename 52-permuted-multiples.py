import itertools


def main():

    x = permuted_multiples()
    print(x)


def permuted_multiples():

    for x in itertools.count(start=1):
        numbers = [x, 2 * x, 3 * x, 4 * x, 5 * x, 6 * x]
        deduped_numbers = list(dict.fromkeys([''.join(sorted(str(digit))) for digit in numbers]))
        if len(deduped_numbers) == 1:
            return min(numbers)
    pass


if __name__ == "__main__":
    main()
