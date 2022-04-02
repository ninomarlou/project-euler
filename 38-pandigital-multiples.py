import itertools
from collections import Counter


def main():

    x = pandigital_multiples()
    print(x)


def pandigital_multiples():
    result = 0
    for i in itertools.count():
        pandigital_n = pandigital_multiples_helper(i)
        if pandigital_n and pandigital_n > result:
            result = pandigital_n
        if i == 55555:  # limit: 5*2=10, 10 repeated 5 times is more than 9 digits
            return result


def pandigital_multiples_helper(n):
    result = ''
    i = 1
    while len(result) < 9:
        result += str(n * i)
        i += 1
    if is_pandigital(result):
        return int(result)
    else:
        return None


def is_pandigital(str_n):
    return Counter(list(str_n)) == Counter(['1', '2', '3', '4', '5', '6', '7', '8', '9'])


if __name__ == "__main__":
    main()
