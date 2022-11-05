def solve(n, t, a, h_list):
    d_min = 100000
    i_min = 0
    for i, h in enumerate(h_list):
        d = abs(a - (t - h * 0.006))
        if d < d_min:
            d_min = d
            i_min = i + 1
    return i_min


def main():
    n = int(input())
    t, a = map(int, input().split())
    h_list = list(map(int, input().split()))
    res = solve(n, t, a, h_list)
    print(res)


def test():
    assert solve(2, 12, 5, [1000, 2000]) == 1
    assert solve(3, 21, -11, [81234, 94124, 52141]) == 3


if __name__ == "__main__":
    test()
    main()
