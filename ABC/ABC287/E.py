def solve(n, s_list):
    s_sorted = list(sorted([(i, s) for i, s in enumerate(s_list)], key=lambda x: x[1]))
    res = [0] * n
    for i in range(n - 1):
        i0, s0 = s_sorted[i]
        i1, s1 = s_sorted[i + 1]
        r = 0
        m = min(len(s0), len(s1))
        for j in range(m):
            if s0[j] == s1[j]:
                r += 1
            else:
                break
        res[i0] = max(res[i0], r)
        res[i1] = max(res[i1], r)
    return res


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    for r in res:
        print(r)


def test():
    assert solve(3, ["abc", "abb", "aac"]) == [2, 2, 1]
    assert solve(11, [
        "abracadabra",
        "bracadabra",
        "racadabra",
        "acadabra",
        "cadabra",
        "adabra",
        "dabra",
        "abra",
        "bra",
        "ra",
        "a"
    ]) == [4, 3, 2, 1, 0, 1, 0, 4, 3, 2, 1]


if __name__ == "__main__":
    test()
    main()
