def solve(n, p_list, q, qa_list, qb_list):
    m = 1
    lm = 1
    while lm <= n:
        lm *= 2
        m += 1
    p_list_list = [[-1] * n for i in range(m)]

    for i in range(n):
        p_list_list[0][i] = p_list[i]
    for j in range(1, m):
        for i in range(n):
            k = p_list_list[j - 1][i]
            if k >= 0:
                p_list_list[j][i] = p_list_list[j - 1][k]
            else:
                p_list_list[j][i] = -1
    # print(p_list_list)
    depth = [-1] * n
    for i in range(n):
        p = i
        d = 0
        for j in range(m - 1, -1, -1):
            if p_list_list[j][p] >= 0:
                d += 2 ** j
                p = p_list_list[j][p]
        depth[i] = d
    # print(depth)

    res = ["No"] * q

    for i in range(q):
        a = qa_list[i]
        b = qb_list[i]
        d = depth[a] - depth[b]
        if d <= 0:
            continue
        p = a
        for j in range(m - 1, -1, -1):
            if d >= 2 ** j:
                p = p_list_list[j][p]
                d -= 2 ** j
        # print(a, p, b)
        if p == b:
            res[i] = "Yes"
    return res


def main():
    n = int(input())
    p_list = [0] * n
    for i in range(n):
        p = int(input())
        p_list[i] = p - 1
    q = int(input())
    qa_list = [0] * n
    qb_list = [0] * n
    for i in range(q):
        a, b = map(int, input().split())
        qa_list[i] = a - 1
        qb_list[i] = b - 1
    res = solve(n, p_list, q, qa_list, qb_list)
    for r in res:
        print(r)


def test():
    assert solve() == 0
    assert solve() == 0
    assert solve() == 0


if __name__ == "__main__":
    #test()
    main()
