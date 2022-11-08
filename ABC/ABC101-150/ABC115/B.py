def solve(n, p_list):
    res = sum(p_list) - max(p_list) // 2
    return res


def main():
    n = int(input())
    p_list = [int(input()) for _ in range(n)]
    res = solve(n, p_list)
    print(res)


def test():
    assert solve(3, [4980, 7980, 6980]) == 15950
    assert solve(4, [4320, 4320, 4320, 4320]) == 15120


if __name__ == "__main__":
    test()
    main()
