def solve(h, w, a):
    res = []
    x = ".ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(h):
        res.append("".join([x[a[i][j]] for j in range(w)]))
    return res


def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    res = solve(h, w, a)
    for r in res:
        print(r)


def test():
    assert solve(2, 3, [[0, 1, 2], [0, 0, 3]]) == [".AB", "..C"]
    assert solve(3, 3, [[24, 0, 0], [0, 25, 0], [0, 0, 26]]) == ["X..", ".Y.", "..Z"]
    assert solve(3, 1, [[2], [9], [4]]) == ["B", "I", "D"]


if __name__ == "__main__":
    test()
    main()
