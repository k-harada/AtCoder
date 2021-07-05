def solve(h, w, s_list):
    res = 0
    for i in range(h - 1):
        for j in range(w - 1):
            r = 0
            if s_list[i][j] == ".":
                r += 1
            if s_list[i + 1][j] == ".":
                r += 1
            if s_list[i][j + 1] == ".":
                r += 1
            if s_list[i + 1][j + 1] == ".":
                r += 1
            if r == 1 or r == 3:
                res += 1
    return res


def main():
    h, w = map(int, input().split())
    s_list = [input() for _ in range(h)]
    res = solve(h, w, s_list)
    print(res)


def test():
    assert solve(5, 5, [".....", ".###.", ".###.", ".###.", "....."]) == 4


if __name__ == "__main__":
    test()
    main()
