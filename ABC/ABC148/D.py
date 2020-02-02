def solve(n, a_list):
    search = 1
    for i in range(n):
        if a_list[i] == search:
            search += 1
    if search == 1:
        return -1
    else:
        return n - search + 1


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [2, 1, 2]) == 1
    assert solve(3, [2, 2, 2]) == -1
    assert solve(10, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == 7
    assert solve(1, [1]) == 0


if __name__ == "__main__":
    test()
    main()
