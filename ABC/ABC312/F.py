from heapq import heappop, heappush


def solve(n, m, tx_list):
    res_max = 0
    res = 0
    c = 0
    h0 = []
    h1 = []
    h2 = []
    for t, x in tx_list:
        if t == 0:
            heappush(h0, x)
            res += x
            c += 1
        elif t == 1:
            heappush(h1, -x)
        else:
            heappush(h2, -x)
    # initial
    while c > m:
        x = heappop(h0)
        res -= x
        c -= 1
    res_max = max(res_max, res)
    d = 0
    while len(h2):
        # add one
        d += 1
        e = heappop(h2)
        for _ in range(min(-e, len(h1))):
            x = heappop(h1)
            heappush(h0, -x)
            res -= x
            c += 1
        while c + d > m and c > 0:
            x = heappop(h0)
            res -= x
            c -= 1
        res_max = max(res_max, res)
    return res_max


def main():
    n, m = map(int, input().split())
    tx_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, m, tx_list)
    print(res)


def test():
    assert solve(8, 4, [(0, 6), (0, 6), (1, 3), (1, 5), (1, 15), (2, 1), (2, 10), (2, 100)]) == 27
    assert solve(5, 5, [(1, 5), (1, 5), (1, 5), (1, 5), (1, 5)]) == 0
    assert solve(12, 6, [
        (2, 2), (0, 1), (0, 9), (1, 3), (1, 5), (1, 3),
        (0, 4), (2, 1), (1, 8), (2, 1), (0, 1), (0, 4)
    ]) == 30


if __name__ == "__main__":
    test()
    main()
