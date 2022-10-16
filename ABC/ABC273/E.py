from collections import defaultdict


def solve(q, query_list):
    p_list = [0] * (q + 1)
    v_list = [-1] * (q + 1)
    node_id = 0
    new_ind = 1
    note = defaultdict(int)
    res = []
    for query in query_list:
        if query[0] == "ADD":
            x = int(query[1])
            p_list[new_ind] = node_id
            node_id = new_ind
            v_list[node_id] = x
            new_ind += 1
        elif query[0] == "DELETE":
            node_id = p_list[node_id]
        elif query[0] == "SAVE":
            y = int(query[1])
            note[y] = node_id
        else:
            z = int(query[1])
            node_id = note[z]
        res.append(v_list[node_id])

    return res


def main():
    q = int(input())
    query_list = [tuple(input().split()) for _ in range(q)]
    res = solve(q, query_list)
    print(" ".join([str(r) for r in res]))


if __name__ == "__main__":
    main()
