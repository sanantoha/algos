
# O(n) time | O(1) space
def is_palindrome(str):
    l = 0
    r = len(str) - 1
    while l < r:
        if str[l] != str[r]:
            return False
        l += 1
        r -= 1

    return True


if __name__ == '__main__':
    print(is_palindrome("abcdcba"))