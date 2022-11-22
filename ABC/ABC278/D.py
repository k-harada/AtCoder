def solve(n, a_list, q, query_list):
    a_list_s = [0] + a_list.copy()
    res = []
    stat = 0
    time = -1
    time_list = [-1] * (n + 1)
    for i, query in enumerate(query_list):
        if query[0] == 1:
            stat = query[1]
            time = i
        elif query[0] == 2:
            if time_list[query[1]] == time:
                a_list_s[query[1]] += query[2]
            else:
                a_list_s[query[1]] = stat + query[2]
                time_list[query[1]] = time
        else:
            if time_list[query[1]] == time:
                res.append(a_list_s[query[1]])
            else:
                res.append(stat)
    # print(res)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, a_list, q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(5, [3, 1, 4, 1, 5], 6, [(3, 2), (2, 3, 4), (3, 3), (1, 1), (2, 3, 4), (3, 3)]) == [1, 8, 5]
    assert solve(1, [1000000000], 8, [
        (2, 1, 1000000000), (2, 1, 1000000000), (2, 1, 1000000000), (2, 1, 1000000000),
        (2, 1, 1000000000), (2, 1, 1000000000), (2, 1, 1000000000), (3, 1)
    ]) == [8000000000]


if __name__ == "__main__":
    test()
    main()
