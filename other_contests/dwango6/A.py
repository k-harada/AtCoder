def solve(n, s_list, t_list, x):
    k = s_list.index(x)
    res = 0
    for i in range(k + 1, n):
        res += t_list[i]
    return res


def main():
    n = int(input())
    s_list = []
    t_list = []
    for _ in range(n):
        s, t_s = input().split()
        s_list.append(s)
        t_list.append(int(t_s))
    x = input()
    res = solve(n, s_list, t_list, x)
    print(res)


def test():
    assert solve(3, ["dwango", "sixth", "prelims"], [2, 5, 25], "dwango") == 30
    assert solve(1, ["abcde"], [1000], "abcde") == 0


if __name__ == "__main__":
    test()
    main()
