from heapq import heappush, heappop


def solve(n, le, a_list):
    h = []
    for a in a_list:
        heappush(h, a)
    if sum(a_list) < le:
        heappush(h, le - sum(a_list))
    res = 0
    while len(h) >= 2:
        a = heappop(h)
        b = heappop(h)
        res += a + b
        heappush(h, a + b)
    return res


def main():
    n, le = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, le, a_list)
    print(res)


def test():
    assert solve(5, 7, [1, 2, 1, 2, 1]) == 16
    assert solve(3, 1000000000000000, [1000000000, 1000000000, 1000000000]) == 1000005000000000


if __name__ == "__main__":
    test()
    main()
