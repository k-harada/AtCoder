def solve(n, w, ab_list):
    ab_list_s = list(sorted(ab_list, key=lambda x: -x[0]))
    total = 0
    res = 0
    for a, b in ab_list_s:
        if total + b <= w:
            total += b
            res += a * b
        elif total < w:
            res += a * (w - total)
            total = w
        # print(total, res)
    # print(res)
    return res


def main():
    n, w = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, w, ab_list)
    print(res)


def test():
    assert solve(3, 5, [(3, 1), (4, 2), (2, 3)]) == 15
    assert solve(4, 100, [(6, 2), (1, 5), (3, 9), (8, 7)]) == 100


if __name__ == "__main__":
    test()
    main()
