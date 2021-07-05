def solve(n, a_list, q, bc_list):
    v_list = [0] * (10 ** 5 + 1)
    s = 0
    for i in range(n):
        a = a_list[i]
        v_list[a] += 1
        s += a
    res_list = []
    for i in range(q):
        b, c = bc_list[i]
        s += v_list[b] * (c - b)
        v_list[c] += v_list[b]
        v_list[b] = 0
        res_list.append(s)
    return res_list


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    q = int(input())
    bc_list = [list(map(int, input().split())) for _ in range(q)]
    res = solve(n, a_list, q, bc_list)
    for r in res:
        print(r)


def test():
    assert solve(4, [1, 2, 3, 4], 3, [[1, 2], [3, 4], [2, 4]]) == [11, 12, 16]
    assert solve(4, [1, 1, 1, 1], 3, [[1, 2], [2, 1], [3, 5]]) == [8, 4, 4]
    assert solve(2, [1, 2], 3, [[1, 100], [2, 100], [100, 1000]]) == [102, 200, 2000]


if __name__ == "__main__":
    test()
    main()
