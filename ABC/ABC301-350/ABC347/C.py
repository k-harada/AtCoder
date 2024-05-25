def solve(n, a, b, d_list):
    c = a + b
    dc_list = []
    for d in d_list:
        dc_list.append(d % c)
    dc_list_us = list(sorted(list(set(dc_list))))
    m = len(dc_list_us)
    if m == 1:
        return "Yes"
    res_min = dc_list_us[-1] - dc_list_us[0]
    for i in range(m - 1):
        res_min = min(res_min, dc_list_us[i] + c - dc_list_us[i + 1])
    if res_min <= a - 1:
        return "Yes"
    else:
        return "No"


def main():
    n, a, b = map(int, input().split())
    d_list = list(map(int, input().split()))
    res = solve(n, a, b, d_list)
    print(res)


def test():
    assert solve(3, 2, 5, [1, 2, 9]) == "Yes"
    assert solve(2, 5, 10, [10, 15]) == "No"
    assert solve(4, 347, 347, [347, 700, 705, 710]) == "Yes"


if __name__ == "__main__":
    test()
    main()
