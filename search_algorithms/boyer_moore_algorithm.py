def preprocess_bad_character(pattern):
    bad_char = {}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = i
    return bad_char


def boyer_moore_search(text, pattern):
    bad_char = preprocess_bad_character(pattern)
    m = len(pattern)
    n = len(text)
    shift = 0

    while shift <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
        if j < 0:
            return shift
        else:
            shift += max(1, j - bad_char.get(text[shift + j], -1))

    return -1


# Test the Boyer-Moore algorithm
if __name__ == "__main__":
    text = "ababcabcabababd"
    pattern = "ababd"
    print("Pattern found at index:", boyer_moore_search(text, pattern))
