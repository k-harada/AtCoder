from collections import deque


def solve(n, needs_list):
    needs_list_s = [[]]
    needs_list_s_rev = [[] for _ in range(n + 1)]
    c_list = [0]
    for i in range(n):
        needs_list_s.append(needs_list[i][1:])
        c_list.append(needs_list[i][0])
        for q in needs_list[i][1:]:
            needs_list_s_rev[q].append(i + 1)
    # print(needs_list_s)
    depth = [-1] * (n + 1)
    depth[1] = 0
    queue = deque([1])
    while len(queue):
        p = queue.popleft()
        # print(p, needs_list_s[p])
        for q in needs_list_s[p]:
            if depth[q] == -1:
                depth[q] = depth[p] + 1
                queue.append(q)
    # print(depth)
    # print(res_list[::-1][:-1])
    queue = deque()
    for i in range(n + 1):
        if depth[i] > 0 and c_list[i] == 0:
            queue.append(i)
    res_list = []
    count_list = [0] * (n + 1)
    while len(queue):
        p = queue.popleft()
        res_list.append(p)
        for q in needs_list_s_rev[p]:
            count_list[q] += 1
            if count_list[q] == c_list[q] and depth[q] > 0:
                queue.append(q)
    res_str = " ".join([str(r) for r in res_list])
    # print(res_str)
    return res_str


def main():
    n = int(input())
    needs_list = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, needs_list)
    print(res)


def test():
    assert solve(6, [[3, 2, 3, 4], [2, 3, 5], [0], [1, 5], [0], [0]]) == "3 5 2 4"
    assert solve(6, [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [0]]) == "6 5 4 3 2"
    assert solve(8, [[1, 5], [1, 6], [1, 7], [1, 8], [0], [0], [0], [0]]) == "5"


if __name__ == "__main__":
    test()
    main()
