def solve(n, p_list):
    p_list_cum_min = [0] * n
    p_list_cum_min[0] = p_list[0]
    for i in range(1, n):
        p_list_cum_min[i] = min(p_list[i], p_list_cum_min[i - 1])

    res = 0
    for i in range(n):
        if p_list[i] <= p_list_cum_min[i]:
            res += 1

    return res


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    print(res)


def test():
    assert solve(5, [4, 2, 5, 1, 3]) == 3
    assert solve(4, [4, 3, 2, 1]) == 4
    assert solve(6, [1, 2, 3, 4, 5, 6]) == 1
    assert solve(8, [5, 7, 4, 2, 6, 8, 1, 3]) == 4
    assert solve(1, [1]) == 1


if __name__ == "__main__":
    test()
    main()
