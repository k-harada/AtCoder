def solve(n, p_list):
    count = [0] * n
    for i, p in enumerate(p_list):
        count[(p - i - 1) % n] += 1
        count[(p - i) % n] += 1
        count[(p - i + 1) % n] += 1
    return max(count)


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    print(res)


def test():
    assert solve(4, [1, 2, 0, 3]) == 4
    assert solve(3, [0, 1, 2]) == 3
    assert solve(10, [3, 9, 6, 1, 7, 3, 8, 0, 5, 4]) == 5


if __name__ == "__main__":
    test()
    main()
