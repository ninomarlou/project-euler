def main():
    x = get_fibonacci_numer(1000)
    print(x)


def get_fibonacci_numer(nr_of_digits):
    f0 = 1
    f1 = 1
    forward = 1
    counter = 2
    while forward == 1:
        tf = f1
        f1 = f0 + f1
        if f1 > 2:
            f0 = tf
        counter += 1
        if len(str(f1)) == nr_of_digits:
            forward = 0

    return counter


if __name__ == "__main__":
    main()
