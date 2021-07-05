def solve(n, s_list):
    res = 1
    for i, s in enumerate(s_list):
        if s == 'OR':
            res += 2 ** (i + 1)
    return res


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    print(res)


def test():
    assert solve(2, ['AND', 'OR']) == 5
    assert solve(5, ['OR', 'OR', 'OR', 'OR', 'OR']) == 63


if __name__ == "__main__":
    test()
    main()
