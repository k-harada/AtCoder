from collections import deque


def solve(n, ab_list):
    g = [[] for _ in range(n + 1)]
    for a, b in ab_list:
        g[a].append(b)
        g[b].append(a)
    # start from 1
    d_list = [-1] * (n + 1)
    d_list[1] = 0
    queue = deque([1])
    while len(queue) > 0:
        p = queue.popleft()
        for q in g[p]:
            if d_list[q] == -1:
                d_list[q] = d_list[p] + 1
                queue.append(q)
    # print(d_list)
    cnt_2 = [0] * 6
    for i in range(1, n + 1):
        cnt_2[d_list[i] % 2] += 1

    if cnt_2[0] <= cnt_2[1]:
        min_01 = 0
    else:
        min_01 = 1

    min_sum = cnt_2[min_01]
    if min_sum <= n // 3:
        res_list = [0] * n
        list_3 = [3 * (k + 1) for k in range(min_sum)]
        list_other = [k for k in range(1, n + 1) if k % 3 != 0] + [3 * (k + 1) for k in range(min_sum, n // 3)]
        for i in range(1, n + 1):
            if d_list[i] % 2 == min_01:
                res_list[i - 1] = list_3.pop()
            else:
                res_list[i - 1] = list_other.pop()
    else:
        res_list = [0] * n
        add_1 = min_sum - (n + 2) // 3
        list_1 = [k + 1 for k in range(n) if k % 3 == 0] + [3 * (k + 1) for k in range(add_1)]
        list_2 = [k + 1 for k in range(n) if k % 3 == 1] + [3 * (k + 1) for k in range(add_1, n // 3)]
        for i in range(1, n + 1):
            if d_list[i] % 2 == min_01:
                res_list[i - 1] = list_1.pop()
            else:
                res_list[i - 1] = list_2.pop()

    return " ".join([str(r) for r in res_list])


def main():
    n = int(input())
    ab_list = [list(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, ab_list)
    print(res)


def test():
    # print(solve(5, [[1, 2], [1, 3], [3, 4], [3, 5]]))
    assert solve(5, [[1, 2], [1, 3], [3, 4], [3, 5]]) == "3 4 1 5 2"


if __name__ == "__main__":
    # test()
    main()
