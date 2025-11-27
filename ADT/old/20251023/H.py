def solve(n, c_list):
    c_min = min(c_list)
    min_i = 0
    for i, c in enumerate(c_list):
        if c == c_min:
            min_i = i + 1
    q, r = n // c_min, n % c_min
    res = [str(min_i)] * q
    # print(res, r)
    for i in range(q):
        for j in range(8, -1, -1):
            k = int(res[i]) - 1
            if c_list[j] - c_list[k] <= r and k < j:
                res[i] = str(j + 1)
                r -= (c_list[j] - c_list[k])

    return int("".join(res))


def main():
    n = int(input())
    c_list = list(map(int, input().split()))
    res = solve(n, c_list)
    print(res)


def test():
    assert solve(5, [5, 4, 3, 3, 2, 5, 3, 5, 3]) == 95
    assert solve(20, [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 99999999999999999999


if __name__ == "__main__":
    test()
    main()
