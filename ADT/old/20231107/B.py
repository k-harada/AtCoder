def solve(n, p_list):
    if n == 1:
        return 0
    m = max(p_list[1:])
    a = p_list[0]
    if a > m:
        return 0
    else:
        return m + 1 - a


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    print(res)


def test():
    assert solve(4, [5, 15, 2, 10]) == 11
    assert solve(4, [15, 5, 2, 10]) == 0
    assert solve(3, [100, 100, 100]) == 1


if __name__ == "__main__":
    test()
    main()
