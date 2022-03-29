def main():

    x = generate_collatz_sequence(1000000)
    print(x)


def generate_collatz_sequence(n):
    cache = {}
    start_points = range(1, n + 1)
    max_length = 0
    longest_chain = []
    collatz_sequence = map(
        lambda x: collatz_sequence_generator_with_cache(x, cache), start_points)
    for sequence in collatz_sequence:
        if sequence[1] > max_length:
            max_length = sequence[1]
            longest_chain = sequence[0]

    return longest_chain


def collatz_sequence_generator_with_cache(n, cache):
    key = n
    n = float(n)
    if key in cache:
        return [n] + cache.get(n)
    result = [n]
    while n != 1:
        if n in cache:
            if key not in cache:
                cache[key] = result[1:] + cache.get(n)
            result = result + cache.get(n)
            return [result[0], len(result)]
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        result.append(n)
    if key not in cache:
        cache[key] = result[1:]
    return [result[0], len(result)]


if __name__ == "__main__":
    main()
