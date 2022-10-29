from heapq import heappop, heappush


def solve(n, w, stp_list):
    h = []
    for i in range(n):
        s, t, p = stp_list[i]
        heappush(h, (s, p, i))
        heappush(h, (t, -p, i))

    needs = 0
    while len(h) > 0:
        t, v, i = heappop(h)
        needs += v
        if needs > w:
            return 'No'
    return 'Yes'


def main():
    n, w = map(int, input().split())
    stp_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, w, stp_list)
    print(res)


def test():
    assert solve(4, 10, [(1, 3, 5), (2, 4, 4), (3, 10, 6), (2, 4, 1)]) == 'No'
    assert solve(4, 10, [(1, 3, 5), (2, 4, 4), (3, 10, 6), (2, 3, 1)]) == 'Yes'
    assert solve(6, 1000000000, [
        (0, 200000, 999999999), (2, 20, 1), (20, 200, 1), (200, 2000, 1), (2000, 20000, 1), (20000, 200000, 1)
    ]) == 'Yes'


if __name__ == "__main__":
    test()
    main()
