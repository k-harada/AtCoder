from itertools import permutations


def solve(n, m, s):
    d = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            dij = 0
            for k in range(m):
                if s[i][k] != s[j][k]:
                    dij += 1
            d[i][j] = dij
            d[j][i] = dij
    for p in permutations(range(n)):
        r = 0
        for q in range(n - 1):
            if d[p[q]][p[q + 1]] != 1:
                r = 1
        if r == 0:
            return "Yes"
    return "No"


def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    res = solve(n, m, s)
    print(res)


def test():
    assert solve(4, 4, ["bbed", "abcd", "abed", "fbed"]) == "Yes"
    assert solve(2, 5, ["abcde", "abced"]) == "No"
    assert solve(8, 4, [
        "fast", "face", "cast", "race",
        "fact", "rice", "nice", "case"
    ]) == "Yes"


if __name__ == "__main__":
    test()
    main()
