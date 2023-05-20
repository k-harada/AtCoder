def solve(n):
    count = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j > n:
                break
            count[i * j] += 1
    # print(count)
    res = 0
    for i in range(1, n + 1):
        res += count[i] * count[n - i]
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(4) == 8
    assert solve(292) == 10886
    assert solve(19876) == 2219958


if __name__ == "__main__":
    test()
    main()
