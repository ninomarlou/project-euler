
import itertools


def main():
    number_set = list(range(1, 11, 1))
    x = create_5_gon_ring(number_set)
    print(x)


def create_5_gon_ring(number_set):
    result = 0
    set_len = 4
    number_set_perms = [[list(z)] for z in set(itertools.permutations(number_set, 3))]
    while set_len > 1:
        temp_number_set_perms = []
        for node in number_set_perms:
            matches = get_new_sequence(number_set, node)
            if matches:
                for match in matches:
                    temp_number_set_perms.append(node + [match])
        number_set_perms = temp_number_set_perms
        set_len -= 1
    for perm in number_set_perms:
        used_digits = [digit for digit in itertools.chain(*perm)]
        remaining_digits = list(set(number_set) - set(used_digits))
        potential_result = [remaining_digits[0], perm[-1][2], perm[0][1]]
        if perm[0][0] < potential_result[0] and sum(perm[0]) == sum(potential_result):
            result_digits = int(''.join([str(digit) for digit in itertools.chain(*perm + [potential_result])]))
            if result_digits > result and len(str(result_digits)) == 16:
                result = result_digits
    return result


def get_new_sequence(number_set, curr_set):
    result = []
    curr_set_middle = curr_set[-1][2]
    curr_set_total = sum(curr_set[-1])
    used_digits = [digit for digit in itertools.chain(*curr_set)]
    remaining_digits = list(set(number_set) - set(used_digits))
    remaining_digit_perms = itertools.permutations(remaining_digits, 2)
    for possible_result in remaining_digit_perms:
        if sum(possible_result) + curr_set_middle == curr_set_total and curr_set[0][0] < possible_result[0]:
            result.append([possible_result[0], curr_set_middle, possible_result[1]])
    return result


if __name__ == '__main__':
    main()
