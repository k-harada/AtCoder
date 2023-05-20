from collections import deque


MOD = 998244353


def solve(q, query_list):
    res = []
    queue = deque([1])
    x = 1
    order = 0
    pow10_list = [1]
    for _ in range(q):
        pow10_list.append((pow10_list[-1] * 10) % MOD)
    for query in query_list:
        if query[0] == 1:
            x *= 10
            x += query[1]
            x %= MOD
            queue.append(query[1])
            order += 1
        elif query[0] == 2:
            p = queue.popleft()
            x -= p * pow10_list[order]
            x %= MOD
            order -= 1
        else:
            res.append(x)
    return res


def main():
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [(3, ), (1, 2), (3, )]) == [1, 12]
    assert solve(3, [(1, 5), (2, ), (3, )]) == [5]


if __name__ == "__main__":
    test()
    main()
