from heapq import heappop, heappush


def solve(n, sc_list):
    h = []
    counts = dict()
    for s, c in sc_list:
        heappush(h, s)
        counts[s] = c
    res = 0
    while len(h):
        s = heappop(h)
        # print(s, counts[s])
        if counts[s] >= 2:
            if 2 * s in counts.keys():
                counts[2 * s] += counts[s] // 2
                res += counts[s] % 2
            else:
                counts[2 * s] = counts[s] // 2
                heappush(h, 2 * s)
                res += counts[s] % 2
        else:
            res += counts[s]
        # print(s, res)
    return res


def main():
    n = int(input())
    sc_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, sc_list)
    print(res)


def test():
    assert solve(3, [(3, 3), (5, 1), (6, 1)]) == 3
    assert solve(3, [(1, 1), (2, 1), (3, 1)]) == 3
    assert solve(1, [(1000000000, 1000000000)]) == 13


if __name__ == "__main__":
    test()
    main()
