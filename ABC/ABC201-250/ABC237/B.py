def solve(h, w, a):
    res = [[a[i][j] for i in range(h)] for j in range(w)]
    res_str = [" ".join([str(res[i][j]) for j in range(h)]) for i in range(w)]
    return res_str


def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    res = solve(h, w, a)
    for r in res:
        print(r)


def test():
    assert solve(4, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) == [
        "1 4 7 10", "2 5 8 11", "3 6 9 12"
    ]
    assert solve(2, 2, [[1000000000, 1000000000], [1000000000, 1000000000]]) == [
        "1000000000 1000000000", "1000000000 1000000000"
    ]


if __name__ == "__main__":
    test()
    main()
