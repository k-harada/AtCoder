MOD = 998244353


def solve(n, k, ck_list):
    cards = [0] * n
    st = 0
    for i in range(k):
        c, p_str = ck_list[i]
        p = int(p_str)
        if c == "R":
            st += 1
            cards[p - 1] = -1
        else:
            cards[p - 1] = 1
    res = 1
    pattern = st
    # print(cards, st)
    for i in range(n):
        if cards[i] == 0:
            res *= pattern
            res %= MOD
        elif cards[i] == 1:
            pattern += 1
        else:
            pattern -= 1
    return res


def main():
    n, k = map(int, input().split())
    ck_list = [tuple(input().split()) for _ in range(k)]
    res = solve(n, k, ck_list)
    print(res)


def test():
    assert solve(3, 2, [("L", "1"), ("R", "2")]) == 1
    assert solve(30, 10, [
        ("R", "6"), ("R", "8"), ("R", "7"), ("R", "25"), ("L", "26"), ("L", "13"), ("R", "14"), ("L", "11"), ("L", "23"), ("R", "30")
    ]) == 343921442


if __name__ == "__main__":
    test()
    main()
