from collections import deque


def solve_f(n, g):

    for i in range(n):
        parent = [-1] * n
        queue = deque([i])
        done = False
        answer = []
        # bfs
        while len(queue) > 0:
            p = queue.popleft()
            for q in g[p]:
                if q == i:
                    r_list = []
                    r = p
                    while r != -1:
                        r_list.append(r)
                        r = parent[r]
                    # check
                    check = 1
                    for r in r_list:
                        check = max(len(set(g[r]).intersection(r_list)), check)
                    if check == 1:
                        return [len(r_list)] + [r + 1 for r in r_list]
                elif parent[q] == -1:
                    parent[q] = p
                    queue.append(q)

    return [-1]


def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a - 1].append(b - 1)
    res = solve_f(n, g)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
