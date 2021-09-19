
# O(n) time | O(n) space
def run_length_encoding(string):
    if string is None or len(string) == 0:
        return ""
    curr_len = 1

    res = []

    for i in range(1, len(string)):
        prev = string[i - 1]
        curr = string[i]

        if prev != curr or curr_len == 9:
            res.append(str(curr_len))
            res.append(prev)
            curr_len = 0

        curr_len += 1

    res.append(str(curr_len))
    res.append(string[len(string) - 1])
    return "".join(res)


if __name__ == '__main__':
    print(run_length_encoding("AAAAAAAAAAAAABBCCCCDD") == "9A4A2B4C2D")
