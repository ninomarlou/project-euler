def main():

    x = tph(285, 100000)
    print(x)


def tph(start, count):
    triangle_numbers = generate_triangle_numbers(start, count)
    pentagonal_numbers = generate_pentagonal_numbers(start, count)
    hexagonal_numbers = generate_hexagonal_numbers(start, count)
    result = set(triangle_numbers).intersection(
        set(pentagonal_numbers)).intersection(set(hexagonal_numbers))
    return result


def generate_triangle_numbers(n, count):
    triangle_numbers = []
    while len(triangle_numbers) < count:
        triangle_numbers.append(int((n * (n + 1)) / 2))
        n += 1
    return triangle_numbers


def generate_pentagonal_numbers(n, count):
    pentagonal_numbers = []
    while len(pentagonal_numbers) < count:
        pentagonal_numbers.append(int((n * ((3 * n) - 1)) / 2))
        n += 1
    return pentagonal_numbers


def generate_hexagonal_numbers(n, count):
    hexagonal_numbers = []
    while len(hexagonal_numbers) < count:
        hexagonal_numbers.append(int(n * ((2 * n) - 1)))
        n += 1
    return hexagonal_numbers


if __name__ == '__main__':
    main()
