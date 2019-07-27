def partial_match_table(word):
    table = [0] * (len(word) + 1)
    table[0] = -1
    i, j = 0, 1

    while j < len(word):
        matched = word[i] == word[j]

        if not matched and i > 0:
            i = table[i]
        else:
            if matched:
                i += 1
            j += 1
            table[j] = i

    return table


def kmp_search(string, pattern):
    table = partial_match_table(pattern)
    i = j = 0
    while i < len(string) and j < len(pattern):
        if string[i] == pattern[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = table[j]

    if j == len(pattern):
        return i - j
    else:
        return None


if __name__ == "__main__":
    r = kmp_search("ABC ABCDAB ABCDABCDABDE", "ABCDABD")
    print(r)
