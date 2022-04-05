import itertools


def main():
    cypher = read_file_as_list('p059_cipher.txt')
    x = xor_decryption(cypher)
    print(x)


def xor_decryption(cypher):
    key_len = 3
    key_table = generate_keys(key_len)
    decrypted_text = decrypt(key_table, cypher)
    ascii_decrypted_text = str_to_ascii(decrypted_text)
    return sum(ascii_decrypted_text)


def str_to_ascii(text):
    return [ord(letter) for letter in text]


def decrypt(key_table, cypher):
    for key in key_table:
        decrypted_text = decrypt_helper(cypher, key)
        if ' the ' in decrypted_text:
            return decrypted_text
    return 'No matches found'


def decrypt_helper(cypher, key):
    key_len = len(key)
    decrypted_text = []
    key_len_rotator = 0
    for char in cypher:
        decrypted_text.append(chr(int(char) ^ key[key_len_rotator]))
        key_len_rotator += 1
        if key_len_rotator == key_len:
            key_len_rotator = 0
    return ''.join(decrypted_text)


def generate_keys(key_len):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    ascii_keys = [ord(letter) for letter in letters]
    key_table = itertools.permutations(ascii_keys, key_len)
    return list(key_table)


def read_file_as_list(path):
    words = []
    with open(path) as f:
        lines = f.readlines()
    f.close()
    return [int(digit) for digit in lines[0].split(",")]


if __name__ == "__main__":
    main()
