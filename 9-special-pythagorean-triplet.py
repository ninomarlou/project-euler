def main():

    x = pythagorean_triplet(1000)
    print(x)


def pythagorean_triplet(n):
    candidates = []
    a = range(1, n - 1)
    for a_digit in a:
        b = range(a_digit + 1, n)
        for b_digit in b:
            c_digit = n - (a_digit + b_digit)
            if c_digit > b_digit:
                candidates.append([a_digit, b_digit, c_digit])
    result_list = list(filter(triplet_check, candidates))[0]
    result = 1
    for digit in result_list:
        result *= digit
    return result


def triplet_check(lst):
    if lst[0]**2 + lst[1]**2 == lst[2]**2:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
