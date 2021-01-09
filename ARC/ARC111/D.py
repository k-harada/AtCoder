def solve(n, m, ab_list, c_list):

    res_list = [""] * m

    # same family
    g = [[] for _ in range(n)]
    for i in range(m):
        a, b = ab_list[i]
        a -= 1
        b -= 1
        if c_list[a] == c_list[b]:
            g[a].append(b)
            g[b].append(a)

    # dfs
    depth = [n] * (n + 1)
    parent = [n] * (n + 1)
    depth[n] = -1
    for i in range(n):
        if depth[i] == n:
            depth[i] = 0
            queue = [i]
            while len(queue):
                p = queue.pop()
                depth[p] = depth[parent[p]] + 1
                for q in g[p]:
                    if depth[q] == n:
                        queue.append(q)
                        parent[q] = p
    # print(depth)

    for i in range(m):
        a, b = ab_list[i]
        a -= 1
        b -= 1
        if c_list[a] > c_list[b]:
            res_list[i] = "->"
        elif c_list[a] < c_list[b]:
            res_list[i] = "<-"
        else:
            if parent[b] == a:
                res_list[i] = "->"
            elif parent[a] == b:
                res_list[i] = "<-"
            else:
                if depth[a] > depth[b]:
                    res_list[i] = "->"
                else:
                    res_list[i] = "<-"

    return res_list


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    c_list = list(map(int, input().split()))
    res_list = solve(n, m, ab_list, c_list)
    for res in res_list:
        print(res)


def test():
    assert solve(3, 3, [(1, 2), (2, 3), (3, 1)], [3, 3, 3]) == ["<-", "<-", "<-"]
    assert solve(3, 2, [(1, 2), (2, 3)], [1, 2, 3]) == ["<-", "<-"]
    assert solve(6, 3, [(1, 2), (4, 3), (5, 6)], [1, 2, 1, 2, 2, 1]) == ["<-", "->", "->"]


if __name__ == "__main__":
    test()
    main()
