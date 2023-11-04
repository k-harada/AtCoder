from collections import deque


def solve(n, m, a_list, b_list):
    g = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b = a_list[i], b_list[i]
        if a == b:
            return "No"
        g[a].append(b)
        g[b].append(a)

    color = [-1] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            queue = deque([i])
            while len(queue):
                p = queue.popleft()
                for q in g[p]:
                    if color[q] == color[p]:
                        return "No"
                    elif color[q] == -1:
                        color[q] = 1 - color[p]
                        queue.append(q)
    return "Yes"


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, m, a_list, b_list)
    print(res)


def test():
    assert solve(3, 2, [1, 2], [2, 3]) == "Yes"
    assert solve(3, 3, [1, 2, 3], [2, 3, 1]) == "No"
    assert solve(10, 1, [1], [1]) == "No"
    assert solve(7, 8, [1, 6, 2, 7, 5, 4, 2, 2], [3, 2, 7, 2, 1, 2, 3, 3]) == "Yes"


if __name__ == "__main__":
    test()
    main()
