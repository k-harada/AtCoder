def solve(h, w, s_list):
    res = 0
    for i in range(h):
        for j in range(w - 1):
            if s_list[i][j] == s_list[i][j + 1] == ".":
                res += 1
    for i in range(h - 1):
        for j in range(w):
            if s_list[i][j] == s_list[i + 1][j] == ".":
                res += 1
    return res


def main():
    h, w = map(int, input().split())
    s_list = [list(input()) for _ in range(h)]
    res = solve(h, w, s_list)
    print(res)


def test():
    assert solve(2, 3, [[".", ".", "#"], ["#", ".", "."]]) == 3
    assert solve(2, 2, [[".", "#"], ["#", "."]]) == 0


if __name__ == "__main__":
    test()
    main()
