def solve(n, x, p_list):
    for i in range(n):
        if p_list[i] == x:
            return i + 1
    return -1


def main():
    n, x = map(int, input().split())
    p_list = list(map(int, input().split()))
    res = solve(n, x, p_list)
    print(res)


def test():
    assert solve(4, 3, [2, 3, 1, 4]) == 2
    assert solve(5, 2, [3, 5, 1, 4, 2]) == 5
    assert solve(6, 6, [1, 2, 3, 4, 5, 6]) == 6


if __name__ == "__main__":
    test()
    main()
