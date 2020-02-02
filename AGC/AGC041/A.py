def solve(n, a, b):
    if (b - a) % 2 == 0:
        return (b - a) // 2
    else:
        # straight_win
        case_1 = a + (b - a - 1) // 2
        # straight_lose
        case_2 = (n - b + 1) + (b - a - 1) // 2
        return min(case_1, case_2)


def main():
    n, a, b = map(int, input().split())
    res = solve(n, a, b)
    print(res)


def test():
    assert solve(5, 2, 4) == 1
    assert solve(5, 2, 3) == 2


if __name__ == "__main__":
    test()
    main()
