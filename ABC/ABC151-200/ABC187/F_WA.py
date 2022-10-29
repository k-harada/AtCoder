def solve(n, m, edge_list):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge_list:
        graph[a].append(b)
        graph[b].append(a)
    reversed_edge_list = [[] for _ in range(n + 1)]
    for a in range(1, n):
        for b in range(a + 1, n + 1):
            if b not in graph[a]:
                reversed_edge_list[a].append(b)
                reversed_edge_list[b].append(a)
    # welsh-powell
    node_list = list(sorted([(i, len(reversed_edge_list[i])) for i in range(n + 1)], key=lambda x: -x[1]))
    color_list = [0] * (n + 1)
    for v_i, _ in node_list:
        if v_i == 0:
            continue
        for c in range(1, n + 1):
            used = False
            for w_i in reversed_edge_list[v_i]:
                if color_list[w_i] == c:
                    used = True
                    break
            if not used:
                color_list[v_i] = c
                break
    # print(color_list)
    return max(color_list)


def main():
    n, m = map(int, input().split())
    edge_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, edge_list)
    print(res)


def test():
    assert solve(3, 2, [(1, 2), (1, 3)]) == 2
    assert solve(4, 6, [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]) == 1
    assert solve(18, 0, []) == 18


if __name__ == "__main__":
    test()
    main()
