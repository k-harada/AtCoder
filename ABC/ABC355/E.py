from collections import deque


def solve(n, left, right):
    g = [[] for _ in range(2 ** n + 1)]
    for i in range(n + 1):
        k = 2 ** i
        p, q = 0, k
        for _ in range(2 ** (n - i)):
            g[p].append(q)
            g[q].append(p)
            p += k
            q += k
    # BFS
    parent_dict = dict()
    parent_dict[left] = -1
    d_dict = dict()
    d_dict[left] = 0
    queue = deque([left])
    while len(queue):
        p = queue.popleft()
        for q in g[p]:
            if q not in parent_dict.keys():
                parent_dict[q] = p
                d_dict[q] = d_dict[p] + 1
                queue.append(q)

    # print(parent_dict)
    res_list = []
    p = right + 1
    while True:
        q = parent_dict[p]
        if q == -1:
            break
        if p < q:
            res_list.append((p, q, -1))
        else:
            res_list.append((q, p, 1))
        p = q
    # print(res_list)
    return res_list


def main():
    n, left, right = map(int, input().split())
    res_list = solve(n, left, right)
    res = 0
    for p, q, f in res_list:
        # print(p, q)
        d = q - p
        i = 0
        while d > 1:
            i += 1
            d //= 2
        j = p // (2 ** i)
        print(f"? {i} {j}")
        r = int(input())
        if f == -1:
            res -= r
        else:
            res += r
        res %= 100

    print(f"! {res}")


def test():
    assert solve(18, 1, 2 ** 18 - 1) == [(0, 262144, 1), (0, 1, -1)]


if __name__ == "__main__":
    test()
    main()
