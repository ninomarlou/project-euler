

def main():

    x = sum_square_difference(100)
    print(x)


def sum_square_difference(n):

    sum_of_squares = 0
    square_of_sum = 0

    for i in range(1, n + 1):
        sum_of_squares += i**2
        square_of_sum += i

    return square_of_sum**2 - sum_of_squares


if __name__ == "__main__":
    main()
