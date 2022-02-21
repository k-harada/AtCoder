def solve(n, a_list):
    count = [0] * (n + 1)
    for a in a_list:
        count[a] += 1

    for r in range(1, n + 1):
        if count[r] == 3:
            return r
    return -1


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [1, 3, 2, 3, 3, 2, 2, 1, 1, 1, 2]) == 3
    assert solve(1, [1, 1, 1]) == 1
    assert solve(4, [3, 2, 1, 1, 2, 4, 4, 4, 4, 3, 1, 3, 2, 1, 3]) == 2


if __name__ == "__main__":
    test()
    main()
