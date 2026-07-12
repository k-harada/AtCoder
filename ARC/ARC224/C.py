from collections import deque


def solve(n, m, uv_list):
    g = [[] for _ in range(n + 1)]
    for u, v in uv_list:
        g[u].append(v)
        g[v].append(u)
    res = [-1] * (n + 1)
    res[1] = 0
    # DFS tour
    parents = [0] * (n + 1)
    visited = [0] * (n + 1)
    queue = deque([1])
    while len(queue):
        p = queue.pop()
        if visited[p]:
            continue
        visited[p] = 1
        for q in g[p]:
            if visited[q]:
                continue
            res[q] = res[p] + 1
            queue.append(q)
    # print(res[1:])
    return res[1:]


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        uv_list = [tuple(map(int, input().split())) for _ in range(m)]
        res = solve(n, m, uv_list)
        print(" ".join([str(r) for r in res]))
    

def test():
    assert solve(6, 7, [(1, 5), (1, 3), (3, 5), (2, 5), (3, 4), (3, 6), (4, 6)]) == [0, 3, 1, 3, 2, 2]
    assert solve(1, 0, []) == [0]
    assert solve(6, 10, [
        (4, 6), (1, 4), (2, 5), (3, 6), (1, 3), 
        (1, 2), (2, 3), (2, 4), (3, 4), (3, 5)
    ]) == [0, 1, 3, 2, 4, 4]


if __name__ == "__main__":
    test()
    main()
