def main():

    x = lychrel_numbers(10000)
    print(x)


def lychrel_numbers(limit):
    result = 0
    numbers = list(range(10, limit + 1))
    for number in numbers:
        if palindrome_check(number) == False:
            result += 1
    return result


def palindrome_check(number):
    for i in range(50):
        rebmun = int(str(number)[::-1])
        check_sum = number + rebmun
        mus_kcehc = int(str(check_sum)[::-1])
        if check_sum == mus_kcehc:
            return True
        else:
            number = check_sum
    return False


if __name__ == "__main__":
    main()
