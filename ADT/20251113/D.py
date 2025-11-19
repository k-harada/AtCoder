def solve(n, qr_list, q, td_list):
    res = []
    for t, d in td_list:
        q, r = qr_list[t - 1]
        res.append(d + (r - d) % q)
    return res


def main():
    n = int(input())
    qr_list = [tuple(map(int, input().split())) for _ in range(n)]
    q = int(input())
    td_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, qr_list, q, td_list)
    for r in res:
        print(r)


def test():
    assert solve(2, [(7, 3), (4, 2)], 5, [
        (1, 1), (1, 3), (1, 4), (1, 15), (2, 7)
    ]) == [3, 3, 10, 17, 10]


if __name__ == "__main__":
    test()
    main()
