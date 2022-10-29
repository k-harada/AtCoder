def solve(n, c_str):
    cum_sum_w_left = [0] * (n + 1)
    cum_sum_r_right = [0] * (n + 1)
    # cum_sum_w_left
    cum_sum_w = 0
    for i in range(n):
        if c_str[i] == "W":
            cum_sum_w += 1
        cum_sum_w_left[i + 1] = cum_sum_w
    # cum_sum_r_right
    cum_sum_r = 0
    for i in range(n - 1, -1, -1):
        if c_str[i] == "R":
            cum_sum_r += 1
        cum_sum_r_right[i] = cum_sum_r
    # print(cum_sum_w_left)
    # print(cum_sum_r_right)
    res = n + 1
    for i in range(n + 1):
        res = min(res, max(cum_sum_w_left[i], cum_sum_r_right[i]))
    # print(res)
    return res


def main():
    n = int(input())
    c_str = input()
    res = solve(n, c_str)
    print(res)


def test():
    assert solve(4, "WWRR") == 2
    assert solve(2, "RR") == 0
    assert solve(8, "WRWWRWRR") == 3


if __name__ == "__main__":
    test()
    main()
