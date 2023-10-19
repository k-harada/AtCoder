def solve(n, m, k_list, a_list):
    queue_list = [[] for _ in range(m)]
    color_list = [[] for _ in range(n + 1)]
    for i in range(m):
        a_ = a_list[i]
        for c in reversed(a_):
            queue_list[i].append(c)
            color_list[c].append(i)
    count = [0] * (n + 1)
    res = 0
    pair_queue = []
    # first turn
    for i in range(m):
        c = queue_list[i].pop()
        count[c] += 1
        if count[c] == 2:
            pair_queue.append(c)
    while len(pair_queue):
        c = pair_queue.pop()
        res += 1
        for i in color_list[c]:
            if len(queue_list[i]) > 0:
                c_i = queue_list[i].pop()
                count[c_i] += 1
                if count[c_i] == 2:
                    pair_queue.append(c_i)
    if res == n:
        return "Yes"
    else:
        return "No"


def main():
    n, m = map(int, input().split())
    k_list = []
    a_list = []
    for _ in range(m):
        k = int(input())
        k_list.append(k)
        a = list(map(int, input().split()))
        a_list.append(a)
    res = solve(n, m, k_list, a_list)
    print(res)


def test():
    assert solve(2, 2, [2, 2], [[1, 2], [1, 2]]) == "Yes"
    assert solve(2, 2, [2, 2], [[1, 2], [2, 1]]) == "No"


if __name__ == "__main__":
    test()
    main()
