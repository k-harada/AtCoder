from collections import deque

LARGE = 10 ** 9 + 7


def solve(n, a_list, b_list):
    # root at 0
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        a = a_list[i] - 1
        b = b_list[i] - 1
        g[a].append(b)
        g[b].append(a)

    parent = [-1] * n
    children = [[] for _ in range(n)]
    depth = [0] * n

    # find parent
    queue = deque([0])
    while len(queue) > 0:
        p = queue.popleft()
        for q in g[p]:
            if q == parent[p]:
                continue
            parent[q] = p
            children[p].append(q)
            depth[q] = depth[p] + 1
            queue.append(q)

    # weight
    weight = [1] * n
    deeper = list(sorted([[i, depth[i]] for i in range(n)], key=lambda x: x[1], reverse=True))
    for i, _ in deeper:
        for j in children[i]:
            weight[i] += weight[j]

    # calc
    res_array = [0] * n
    # P(i is not hole | i is white) = (other than one child( + parent) are all white)
    for i in range(1, n):
        for j in children[i]:
            res_array[n - 1 - weight[j]] += 1
        res_array[weight[i] - 1] += 1
        res_array[n - 1] -= len(children[i])
    for j in children[0]:
        res_array[n - 1 - weight[j]] += 1
    res_array[n - 1] -= len(children[0]) - 1
    # print(res_array)

    res_a = pow(2, n - 1, LARGE) * n
    res_a %= LARGE
    # print(res_a)
    for i in range(n):
        res_a -= pow(2, n - i - 1, LARGE) * res_array[i]
        res_a %= LARGE
        # print(res_a)
    res_b = pow(2, n, LARGE)

    res = res_a * pow(res_b, LARGE - 2, LARGE) % LARGE
    # print(res_a, res_b)
    return res


def main():
    n = int(input())
    a_list = [0] * (n - 1)
    b_list = [0] * (n - 1)
    for i in range(n - 1):
        a, b = map(int, input().split())
        a_list[i] = a
        b_list[i] = b
    res = solve(n, a_list, b_list)
    print(res)


def test():
    assert solve(3, [1, 2], [2, 3]) == 125000001
    assert solve(4, [1, 2, 3], [2, 3, 4]) == 375000003
    assert solve(4, [1, 1, 1], [2, 3, 4]) == 250000002


if __name__ == "__main__":
    test()
    main()
