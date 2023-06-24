def solve(n, s_list):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            ss = s_list[i] + s_list[j]
            m = len(ss)
            r = 0
            for k in range(m):
                if ss[k] != ss[m - 1 - k]:
                    r += 1
            if r == 0:
                return "Yes"
    return "No"


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    print(res)


def test():
    assert solve(5, ["ab", "ccef", "da2", "a", "fe"]) == "Yes"
    assert solve(3, ["a", "b", "aba"]) == "No"
    assert solve(2, [
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ]) == "Yes"


if __name__ == "__main__":
    test()
    main()
