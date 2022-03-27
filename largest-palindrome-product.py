
def main():
    x = largest_palindrom_product(100, 1000)
    print(x)


def largest_palindrom_product(min, max):
    max_result = 0
    for i in range(min, max):
        for j in range(min, max):
            result = i * j
            str_result = str(result)
            if str_result == str_result[::-1] and result > max_result:
                max_result = result
    return max_result


if __name__ == "__main__":
    main()
