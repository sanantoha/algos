
# O(n + m) time | O(n) space
def generate_document(characters, document):
    if len(document) > len(characters):
        return False

    chars_map = {}
    for i in range(len(characters)):
        c = characters[i]
        if c in chars_map:
            chars_map[c] += 1
        else:
            chars_map[c] = 1

    for i in range(len(document)):
        c = document[i]
        if c not in chars_map:
            return False
        else:
            if chars_map[c] <= 0:
                return False
            chars_map[c] -= 1

    return True


# O(m * (n + m)) time | O(1) space
def generate_document1(characters, document):
    if len(document) > len(characters):
        return False

    for i in range(len(document)):
        c = document[i]
        freq_doc = find_freq(document, c)
        freq_chars = find_freq(characters, c)
        if freq_doc > freq_chars:
            return False

    return True


def find_freq(str, target):
    count = 0
    for c in str:
        if target == c:
            count += 1
    return count


if __name__ == '__main__':
    print(generate_document("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))
    print(generate_document1("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))
