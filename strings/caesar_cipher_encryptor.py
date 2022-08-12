
# O(n) time | O(1) space
def caesar_cipher_encryptor(string, key):
    res = []
    key %= 26
    for idx in range(len(string)):
        num = ord(string[idx])
        new_num = num + key if num + key <= 122 else (num + key) % 122 + 96
        res.append(chr(new_num))

    return "".join(res)


if __name__ == '__main__':
    print(caesar_cipher_encryptor("xyz", 2) == "zab")
    print(caesar_cipher_encryptor("abc", 52) == "abc")
