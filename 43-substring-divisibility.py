import itertools
import functools


def main():

    x = substring_divisibility()
    print(x)


def substring_divisibility():

    result = 0
    perms = [''.join(n) for n in list(itertools.permutations(
        '9876543210')) if check_divisibility(n)]

    return sum([int(n) for n in perms])


def check_divisibility(n):
    if int(n[1] + n[2] + n[3]) % 2 == 0:
        if int(n[2] + n[3] + n[4]) % 3 == 0:
            if int(n[3] + n[4] + n[5]) % 5 == 0:
                if int(n[4] + n[5] + n[6]) % 7 == 0:
                    if int(n[5] + n[6] + n[7]) % 11 == 0:
                        if int(n[6] + n[7] + n[8]) % 13 == 0:
                            if int(n[7] + n[8] + n[9]) % 17 == 0:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
