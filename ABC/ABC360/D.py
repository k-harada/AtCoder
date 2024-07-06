from bisect import bisect_left, bisect_right


def solve(n, t, s, x_list):
    res = 0
    left_list = []
    right_list = []
    for i in range(n):
        if s[i] == "0":
            left_list.append(x_list[i])
        else:
            right_list.append(x_list[i])
    left_list_s = list(sorted(left_list))
    right_list_s = list(sorted(right_list))
    for a in right_list_s:
        res += bisect_right(left_list_s, a + 2 * t) - bisect_left(left_list_s, a)
    # print(res)
    return res


def main():
    n, t = map(int, input().split())
    s = input()
    x_list = list(map(int, input().split()))
    res = solve(n, t, s, x_list)
    print(res)


def test():
    assert solve(6, 3, "101010", [-5, -1, 0, 1, 2, 4]) == 5
    assert solve(13, 656320850, "0100110011101", [
        -900549713, -713494784, -713078652, -687818593, -517374932,
        -498415009, -472742091, -390030458, -379340552, -237481538,
        -44636942, 352721061, 695864366
    ]) == 14


if __name__ == "__main__":
    test()
    main()
