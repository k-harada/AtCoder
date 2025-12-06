def solve(n, a_list):
    m = a_list[0] + 1
    for i in range(1, n):
        if m > i + 1:
            m = max(m, i + 1 + a_list[i])
    return min(m - 1, n)


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(4, [3, 1, 4, 1]) == 4
    assert solve(9, [1, 4, 1, 4, 2, 1, 3, 5, 6]) == 1
    assert solve(10, [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 5


if __name__ == "__main__":
    test()
    main()
