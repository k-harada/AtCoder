def solve(n, wx_list):
    count = [0] * 24
    for w, x in wx_list:
        count[x] += w
    s_max = sum(count[:9])
    s = s_max
    for i in range(9, 33):
        s += count[i % 24]
        s -= count[(i - 9) % 24]
        s_max = max(s_max, s)
    return s_max


def main():
    n = int(input())
    wx_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, wx_list)
    print(res)


def test():
    assert solve(3, [(5, 0), (3, 3), (2, 18)]) == 8
    assert solve(2, [(1, 10), (100000, 20)]) == 100000
    assert solve(6, [(31, 3), (20, 8), (11, 5), (4, 3), (47, 14), (1, 18)]) == 67


if __name__ == "__main__":
    test()
    main()
