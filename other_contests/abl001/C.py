import networkx as nx


def solve(n, m, ab_list):
    g = nx.Graph()
    g.add_nodes_from(list(range(1, n + 1)))
    g.add_edges_from(ab_list)
    res = nx.algorithms.components.number_connected_components(g) - 1
    return res


def main():
    n, m = map(int, input().split())
    ab_list = []
    for _ in range(m):
        ab_list.append(tuple(map(int, input().split())))
    res = solve(n, m, ab_list)
    print(res)


def test():
    assert solve(3, 1, [(1, 2)]) == 1


if __name__ == "__main__":
    test()
    main()
