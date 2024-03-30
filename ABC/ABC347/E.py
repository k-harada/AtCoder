def solve(n, q, x_list):
    res_list = [0] * n
    ind_list = [[] for _ in range(n)]
    c_list = []
    state = [0] * n
    c = 0
    for i, x in enumerate(x_list):
        ind_list[x - 1].append(i)
        if state[x - 1] == 0:
            c += 1
            state[x - 1] = 1
        else:
            c -= 1
            state[x - 1] = 0
        c_list.append(c)
    c_list_cum = [0]
    for i in range(q):
        c_list_cum.append(c_list_cum[-1] + c_list[i])
    # print(ind_list)
    # print(c_list_cum)
    for i in range(n):
        if len(ind_list[i]) % 2 == 1:
            ind_list[i].append(q)
        m = len(ind_list[i]) // 2
        # print(ind_list[i])
        for j in range(m):
            x, y = ind_list[i][2 * j], ind_list[i][2 * j + 1]
            # print(x, y)
            res_list[i] += c_list_cum[y] - c_list_cum[x]
    # print(res_list)
    return " ".join([str(r) for r in res_list])


def main():
    n, q = map(int, input().split())
    x_list = list(map(int, input().split()))
    res = solve(n, q, x_list)
    print(res)


def test():
    assert solve(3, 4, [1, 3, 3, 2]) == "6 2 2"
    assert solve(4, 6, [1, 2, 3, 2, 4, 2]) == "15 9 12 7"


if __name__ == "__main__":
    test()
    main()
