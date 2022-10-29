from heapq import heappop, heappush


def solve(q, query_list):
    res = []
    h = []
    add = 0
    sub = 0
    for i, query in enumerate(query_list):
        if query[0] == 1:
            heappush(h, query[1] - sub)
        elif query[0] == 2:
           add += query[1]
           sub += query[1]
        else:
            r = heappop(h) + add
            res.append(r)
    return res


def main():
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(5, [(1, 3), (1, 5), (3,), (2, 2), (3,)]) == [3, 7]
    assert solve(6, [
        (1, 1000000000), (2, 1000000000), (2, 1000000000), (2, 1000000000), (2, 1000000000), (3,)
    ]) == [5000000000]


if __name__ == "__main__":
    test()
    main()
