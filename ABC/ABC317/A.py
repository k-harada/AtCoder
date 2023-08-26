def solve(n, h, x, p_list):
    for i in range(n):
        if p_list[i] + h >= x:
            return i + 1
    return -1


def main():
    n, h, x = map(int, input().split())
    p_list = list(map(int, input().split()))
    res = solve(n, h, x, p_list)
    print(res)


def test():
    assert solve(3, 100, 200, [50, 200, 999]) == 2
    assert solve(2, 10, 21, [10, 999]) == 2
    assert solve(10, 500, 999, [38, 420, 490, 585, 613, 614, 760, 926, 945, 999]) == 4


if __name__ == "__main__":
    test()
    main()
