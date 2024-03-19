def solve(n, x, a_list):
    if n == 1:
        return x
    res_dict = dict()
    for i in range(n - 1, -1, -1):
        a = a_list[i]
        x_low = (x // a) * a
        x_high = x_low + a
        if i == n - 1:
            res_dict[x_low] = x_low // a
            res_dict[x_high] = x_high // a
        elif i > 0:
            r = a_list[i + 1] // a_list[i]
            c_low = (x_low // a) % r
            if c_low > 0:
                x_low_low = x_low - c_low * a
                x_low_high = x_low + (r - c_low) * a
            else:
                x_low_low = x_low
                x_low_high = x_low
            # print(i, r, a_list[i], x, x_low_low, x_low_high, res_dict)
            res_dict[x_low] = min(c_low + res_dict[x_low_low], r - c_low + res_dict[x_low_high])
            c_high = (x_high // a) % r
            if c_high > 0:
                x_high_low = x_high - c_high * a
                x_high_high = x_high + (r - c_high) * a
            else:
                x_high_low = x_high
                x_high_high = x_high
            res_dict[x_high] = min(c_high + res_dict[x_high_low], r - c_high + res_dict[x_high_high])
        else:
            r = a_list[1]
            c = x % a_list[1]
            res_dict[x] = min(c + res_dict[x - c], r - c + res_dict[x - c + r])
        # print(res_dict)
    res = res_dict[x]
    return res


def main():
    n, x = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, x, a_list)
    print(res)


def test():
    assert solve(3, 87, [1, 10, 100]) == 5
    assert solve(2, 49, [1, 7]) == 7
    assert solve(10, 123456789012345678, [
        1, 100, 10000, 1000000, 100000000, 10000000000,
        1000000000000, 100000000000000, 10000000000000000, 1000000000000000000
    ]) == 233


if __name__ == "__main__":
    test()
    main()
