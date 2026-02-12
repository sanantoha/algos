from strings.caesar_cipher_encryptor import caesar_cipher_encryptor


def test_caesar_cipher_encryptor_case1():
    assert caesar_cipher_encryptor("xyz", 2) == "zab"


def test_caesar_chipher_encryptor_case2():
    assert caesar_cipher_encryptor("abc", 52) == "abc"