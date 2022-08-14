def solve(n, p_list):
    res = 0
    p = n
    while p != 1:
        p = p_list[p - 2]
        res += 1
    return res


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    print(res)


def test():
    assert solve(3, [1, 2]) == 2
    assert solve(10, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
    assert solve(10, [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1


if __name__ == "__main__":
    test()
    main()
