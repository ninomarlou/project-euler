import itertools
import sympy


def main():

    x = prime_permutations(4, 3330)
    print(x)

# 2969


def prime_permutations(digit_count, interval):
    result = []
    digits = '1234567890'
    elements = []
    for i in range(0, digit_count, 1):
        elements.append(digits)
    prime_digit_cartesian = [x for x in itertools.product(
        *elements) if sympy.isprime(int(''.join(x))) and len(str(int(''.join(x)))) == 4]

    digits_dict = {}
    for digit in prime_digit_cartesian:
        key = ''.join(sorted(digit))
        perms_list = digits_dict.get(key, [])
        perms_list.append(int(''.join(digit)))
        digits_dict[key] = perms_list

    for key in digits_dict:
        items = digits_dict.get(key)
        if len(items) > 2:
            sequential_elements = sequence_check(items, interval)
            if len(sequential_elements) != 0:
                for element in sequential_elements:
                    result.append(int(''.join([str(e) for e in element])))

    return result


def sequence_check(sequence, interval):
    result = []
    for i in range(0, len(sequence), 1):
        current_element = sequence[i]
        sequential_elements = [current_element]
        forward = 1
        while forward == 1:
            next_element = current_element + interval
            if next_element in sequence:
                sequential_elements.append(next_element)
                current_element = next_element
            else:
                if len(sequential_elements) == 3:
                    result.append(sequential_elements)
                forward = 0
    return result


if __name__ == '__main__':
    main()
