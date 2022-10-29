def solve(s, t):
    res = 0
    for a in range(s + 1):
        for b in range(s + 1):
            for c in range(s + 1):
                if a + b + c <= s and a * b * c <= t:
                    res += 1
    return res


def main():
    s, t = map(int, input().split())
    res = solve(s, t)
    print(res)


def test():
    assert solve(1, 0) == 4
    assert solve(2, 5) == 10
    assert solve(10, 10) == 213
    assert solve(30, 100) == 2471


if __name__ == "__main__":
    test()
    main()
