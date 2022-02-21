def solve(n, a_list):
    r_list = [0]
    a_total = 0
    for a in a_list:
        a_total += a
        a_total %= 360
        r_list.append(a_total)
    r_list_s = list(sorted(r_list))
    a_max = 360 - r_list_s[-1]
    for i in range(len(r_list_s) - 1):
        a_max = max(a_max, r_list_s[i + 1] - r_list_s[i])
    return a_max


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
