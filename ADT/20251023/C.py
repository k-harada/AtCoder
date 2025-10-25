def solve(n, s_list):
    ans_list = [1] * (1001)
    for a in range(1, 350):
        for b in range(1, 350):
            s = 4 * a * b + 3 * a + 3 * b
            if s < 1001:
                ans_list[s] = 0
    res = 0
    for s in s_list:
        res += ans_list[s]
    return res


def main():
    n = int(input())
    s_list = list(map(int, input().split()))
    res = solve(n, s_list)
    print(res)


def test():
    assert solve(3, [10, 20, 39]) == 1
    assert solve(5, [666, 777, 888, 777, 666]) == 3


if __name__ == "__main__":
    test()
    main()
