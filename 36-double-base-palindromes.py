import sympy
from eulerlib import primes


def main():

    x = double_base_palindromes()
    print(x)


def double_base_palindromes():
    dec_palindromes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = 0

    # 2 digits
    for i in range(1, 10):
        dec_palindromes.append(int(str(i) + str(i)))
    # 3 digits
    for i in range(1, 10):
        for j in range(10):
            dec_palindromes.append(int(str(i) + str(j) + str(i)))
    # 4 digits
    for i in range(1, 10):
        for j in range(10):
            dec_palindromes.append(int(str(i) + str(j) + str(j) + str(i)))
    # 5 digits
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                dec_palindromes.append(
                    int(str(i) + str(j) + str(k) + str(j) + str(i)))
    # 6 digits
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                dec_palindromes.append(
                    int(str(i) + str(j) + str(k) + str(k) + str(j) + str(i)))

    for dec_palindrome in dec_palindromes:
        if f"{dec_palindrome:b}" == f"{dec_palindrome:b}"[::-1]:
            result += dec_palindrome

    return result


if __name__ == "__main__":
    main()
