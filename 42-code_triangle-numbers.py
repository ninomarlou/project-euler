def main():

    words = read_file_as_list('p042_words.txt')
    letter_dict = generate_letter_dictionary()
    x = code_triangle_numbers(words, letter_dict)
    print(x)


def code_triangle_numbers(words, letter_dict):
    result = 0
    for word in words:
        if is_triangle(get_word_value(word, letter_dict)):
            result += 1
    return result


def is_triangle(word_value):
    n = 1
    while n <= word_value:
        t = (n * (n + 1)) / 2
        if t == word_value:
            return True
        n += 1
    return False


def coded_triangle_numers(n):

    pass


def get_word_value(word, letter_dict):
    result = 0
    for l in word:
        result += letter_dict.get(l)
    return result


def generate_letter_dictionary():
    letter = 'abcdefghijklmnopqrstuvwxyz'
    letter_dict = {}
    for i in range(0, len(letter), 1):
        letter_dict[letter[i].capitalize()] = i + 1
    return letter_dict


def read_file_as_list(path):
    words = []
    with open(path) as f:
        lines = f.readlines()
    f.close()
    for line in lines:
        for word in line.split(","):
            words.append(word.strip('"'))
    return words


if __name__ == "__main__":
    main()
