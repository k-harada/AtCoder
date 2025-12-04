def solve(n, m, s, t, lr_list):
    count_list = [0] * (n + 2)
    for left, right in lr_list:
        count_list[left] += 1
        count_list[right + 1] += 1
    # print(count_list)
    count_list_cum = [0] * (n + 2)
    for i in range(1, n + 2):
        count_list_cum[i] = (count_list_cum[i - 1] + count_list[i]) % 2
    # print(count_list_cum)
    res = []
    for i in range(1, n + 1):
        if count_list_cum[i] == 0:
            res.append(s[i - 1])
        else:
            res.append(t[i - 1])
    return "".join(res)


def main():
    n, m = map(int, input().split())
    s = input()
    t = input()
    lr_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, s, t, lr_list)
    print(res)


def test():
    assert solve(
        5, 3, "apple", "lemon", [
            (2, 4), (1, 5), (5, 5)
        ]) == "lpple"
    assert solve(10, 5, "lemwrbogje", "omsjbfggme", [
        (5, 8), (4, 8), (1, 3), (6, 6), (1, 4)
    ]) == "lemwrfogje"


if __name__ == "__main__":
    test()
    main()
