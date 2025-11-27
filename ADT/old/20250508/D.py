def solve(n, a_list):
    r_list = [0]
    for a in a_list:
        r_list.append((r_list[-1] + a) % 360)
    r_list_s = sorted(r_list)
    r_list_s.append(360)
    res = 0
    m = len(r_list_s)
    for i in range(m - 1):
        res = max(res, r_list_s[i + 1] - r_list_s[i])
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(4, [90, 180, 45, 195]) == 120
    assert solve(1, [1]) == 359
    assert solve(10, [215, 137, 320, 339, 341, 41, 44, 18, 241, 149]) == 170


if __name__ == "__main__":
    test()
    main()
