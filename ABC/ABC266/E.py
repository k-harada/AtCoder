def solve(n):
    res = [0.0] * (n + 1)
    for i in range(n - 1, -1, -1):
        for j in range(1, 7):
            if j > res[i + 1]:
                res[i] += j / 6
            else:
                res[i] += res[i + 1] / 6
    # print(res[0])
    return res[0]


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(1) == 3.5
    assert solve(2) == 4.25
    assert solve(10) == 5.6502176688


if __name__ == "__main__":
    # test()
    main()
