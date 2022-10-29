from collections import deque


LARGE = 10 ** 9 + 7


def solve(n, m, ab_list):
    g = [[] for _ in range(n + 1)]
    for a, b in ab_list:
        g[a].append(b)
        g[b].append(a)

    dist = [n + 1] * (n + 1)
    dist[1] = 0
    count = [0] * (n + 1)
    count[1] = 1
    # BFS
    queue = deque([1])
    while len(queue):
        p = queue.popleft()
        for q in g[p]:
            if dist[q] > dist[p] + 1:
                dist[q] = dist[p] + 1
                count[q] = count[p]
                queue.append(q)
            elif dist[q] == dist[p] + 1:
                count[q] += count[p]
                count[q] %= LARGE
            else:
                pass

    return count[n]


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, ab_list)
    print(res)


def test():
    assert solve(4, 5, [(2, 4), (1, 2), (2, 3), (1, 3), (3, 4)]) == 2
    assert solve(4, 3, [(1, 3), (2, 3), (2, 4)]) == 1
    assert solve(2, 0, []) == 0


if __name__ == "__main__":
    test()
    main()
