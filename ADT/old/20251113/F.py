from itertools import permutations


def solve(n, m, s_list):
    d = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            d_ij = 0
            for k in range(m):
                if s_list[i][k] != s_list[j][k]:
                    d_ij += 1
            d[i][j] = d_ij
    for p in permutations(list(range(n))):
        r = 0
        for k in range(n - 1):
            if d[p[k]][p[k + 1]] != 1:
                r = 1
        if r == 0:
            return "Yes"
    return "No"


def main():
    n, m = map(int, input().split())
    s_list = [input() for _ in range(n)]
    res = solve(n, m, s_list)
    print(res)


def test():
    assert solve(4, 4, [
        "bbed",
        "abcd",
        "abed",
        "fbed"
    ]) == "Yes"
    assert solve(2, 5, ["abcde", "abced"]) == "No"
    assert solve(8, 4, [
        "fast",
        "face",
        "cast",
        "race",
        "fact",
        "rice",
        "nice",
        "case"
    ]) == "Yes"


if __name__ == "__main__":
    # test()
    main()
