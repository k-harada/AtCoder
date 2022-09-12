def solve(n, q, p_list, query_list):
    children = [[] for _ in range(n + 1)]
    parents_list = [0, 0] + p_list
    for i, p in enumerate(p_list):
        children[p].append(i + 2)
    len_children = [len(children[i]) for i in range(n + 1)]
    status = [0] * (n + 1)
    res = []
    for query in query_list:
        r = 0
        for b in query[1:]:
            status[b] = 1

        for b in query[1:]:
            if status[parents_list[b]] == 0:
                # 自分と子どもたちを裏返す
                r += len_children[b] + 1
            else:
                # 1回分キャンセル
                r -= 1
                # 子どもたちを裏返す
                r += len_children[b]
        for b in query[1:]:
            status[b] = 0
        res.append(r)

    # DFS tour
    # queue = [1]
    # tour = []
    # while len(queue):
    #     p = queue.pop()
    #     tour.append(p)
    #     for q in children[p]:
    #         queue.append(q)
    # print(tour)

    return res


def main():
    n, q = map(int, input().split())
    p_list = list(map(int, input().split()))
    query_list = [list(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, p_list, query_list)
    for r in res:
        print(r)


def test():
    assert solve(6, 6, [1, 1, 2, 2, 5], [
        [6, 1, 2, 3, 4, 5, 6],
        [3, 2, 5, 6],
        [1, 3],
        [3, 1, 2, 3],
        [3, 4, 5, 6],
        [4, 2, 3, 4, 5]
    ]) == [1, 2, 1, 3, 2, 3]


if __name__ == "__main__":
    # test()
    main()
