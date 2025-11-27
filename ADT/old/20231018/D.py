def solve(n, p_list):
    res = 0
    q = n
    while q > 1:
        res += 1
        p = p_list[q - 2]
        q = p
    return res


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    print(res)


def test():
    assert solve(3, [1, 2]) == 2
    assert solve(4, [1, 1, 1, 1]) == 1
    assert solve(10, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9


if __name__ == "__main__":
    test()
    main()
