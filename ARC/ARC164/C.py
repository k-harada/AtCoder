from heapq import heappop, heappush


def solve(n, ab_list):
    h = []
    for a, b in ab_list:
        heappush(h, (b - a, a, b))
    res = 0
    for _ in range(n):
        d, a, b = heappop(h)
        heappush(h, (a - b, b, a))
        d, a, b = heappop(h)
        res += a
    # print(res)
    return res


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, ab_list)
    print(res)


def test():
    assert solve(3, [(6, 4), (2, 1), (5, 3)]) == 12
    assert solve(5, [
        (166971716, 552987438), (219878198, 619875818), (918378176, 518975015),
        (610749017, 285601372), (701849287, 307601390)
    ]) == 3078692091


def test_large():
    assert solve(200000, [(i + 1, i + 1) for i in range(200000)]) == 100000 * 200001


if __name__ == "__main__":
    test()
    # test_large()
    main()
