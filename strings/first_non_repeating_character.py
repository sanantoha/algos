# O(n) time | O(1) space (because chars length only 26 symbols (input only lowercase alphabetical symbols)
def first_non_repeating_character(string):
    chars = {}
    for c in string:
        chars[c] = chars.get(c, 0) + 1

    for i, c in enumerate(string):
        if chars[c] == 1:
            return i

    return -1


if __name__ == '__main__':
    print(first_non_repeating_character("abcdcaf"))