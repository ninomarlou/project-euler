import itertools


def main():
    choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    place = 1000000
    x = lexographic_permutations(choices, place)
    print(x)


def lexographic_permutations(choices, place):
    perm = list(itertools.permutations(choices))
    return perm[place - 1]


if __name__ == "__main__":
    main()
