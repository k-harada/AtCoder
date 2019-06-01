def build_tree(N, edge_list):

    G = dict()
    for i in range(1, N+1):
        G[i] = dict()

    for i in range(N-1):
        a, b = edge_list[i]
        G[a][b] = 1
        G[b][a] = 1

    leaves = []
    for i in range(1, N+1):
        if len(G[i].keys()) == 1:
            leaves.append(i)

    return G, leaves


def pop_leaf_loop(G, leaves, c_list):

    res_list = [""]*N

    for i in range(N):
        leaf = leaves[i]
        res_list[leaf-1] = str(c_list[i])
        for j in G[leaf]:
            del G[j][leaf]
            if len(G[j].keys()) == 1:
                leaves.append(j)

    return res_list


if __name__ == "__main__":
    N = int(input())
    edge_list = [[] for _ in range(N-1)]
    for i in range(N-1):
        edge_list[i] = list(map(int, input().split()))
    c_list = list(sorted(list(map(int, input().split()))))
    G, leaves = build_tree(N, edge_list)
    res_list = pop_leaf_loop(G, leaves, c_list)
    print(sum(c_list) - max(c_list))
    print(" ".join(res_list))
