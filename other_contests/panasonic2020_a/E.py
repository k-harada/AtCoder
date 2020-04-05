def partial_match_table_mod(word):
    table = [0] * (len(word) + 1)
    table[0] = -1
    i, j = 0, 1

    while j < len(word):
        matched = (word[i] == word[j]) and (word[i] != "?")

        if not matched and i > 0:
            i = table[i]
        else:
            if matched:
                i += 1
            j += 1
            table[j] = i

    return table


def kmp_search_mod(string, pattern):
    table = partial_match_table_mod(pattern)
    i = j = 0
    while i < len(string) and j < len(pattern):
        if string[i] == pattern[j] or string[i] == "?" or pattern[j] == "?":
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


def solve_partial(s1, s2, s3):
    s1_add = s1 + "?" * len(s2)
    k1 = kmp_search_mod(s1_add, s2)
    assert k1 is not None
    s1_res = list(s1_add[:max(k1 + len(s2), len(s1))])
    for i in range(k1, min(len(s1), k1 + len(s2))):
        if s1[i] != s2[i - k1]:
            if s1[i] != "?":
                s1_res[i] = s1[i]
            else:
                s1_res[i] = s2[i - k1]
    for i in range(len(s1), k1 + len(s2)):
        s1_res[i] = s2[i - k1]
    s12 = "".join(s1_res)
    s12_add = s12 + "?" * len(s3)
    # print(s12_add)
    k2 = kmp_search_mod(s12_add, s3)
    assert k2 is not None
    # print(max(k2 + len(s3), len(s12)))
    return max(k2 + len(s3), len(s12))


def solve(s1, s2, s3):
    res = len(s1) + len(s2) + len(s3)
    res = min(res, solve_partial(s1, s2, s3))
    res = min(res, solve_partial(s1, s3, s2))
    res = min(res, solve_partial(s2, s1, s3))
    res = min(res, solve_partial(s2, s3, s1))
    res = min(res, solve_partial(s3, s1, s2))
    res = min(res, solve_partial(s3, s2, s1))
    return res


def main():
    s1 = input()
    s2 = input()
    s3 = input()
    res = solve(s1, s2, s3)
    print(res)
    # for r in res:
    #     print(r)


def test():
    assert solve("a?c", "der", "cod") == 7
    assert solve("atcoder", "atcoder", "???????") == 7


if __name__ == "__main__":
    test()
    main()
