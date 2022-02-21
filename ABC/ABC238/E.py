from collections import deque


def solve(n, q, lr_list):
    g = [[] for _ in range(n + 1)]
    for l, r in lr_list:
        g[l - 1].append(r)
        g[r].append(l - 1)

    # BFS
    visited = [0] * (n + 1)
    queue = deque([0])
    visited[0] = 1
    while len(queue):
        p = queue.popleft()
        for q in g[p]:
            if visited[q] == 0:
                visited[q] = 1
                queue.append(q)

    if visited[n] == 1:
        return "Yes"
    else:
        return "No"


def main():
    n, q = map(int, input().split())
    lr_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, lr_list)
    print(res)


def test():
    assert solve(3, 3, [(1, 2), (2, 3), (2, 2)]) == "Yes"
    assert solve(4, 3, [(1, 3), (1, 2), (2, 3)]) == "No"
    assert solve(4, 4, [(1, 1), (2, 2), (3, 3), (1, 4)]) == "Yes"


if __name__ == "__main__":
    test()
    main()
