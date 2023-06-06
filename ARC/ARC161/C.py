from collections import deque


def solve_sub(n, ab_list, s):
    res = [""] * n
    g = [[] for _ in range(n)]
    for a, b in ab_list:
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    # 0を根とする
    parents = [-1] * n
    children = [[] for _ in range(n)]
    queue = deque([0])
    order = [0]
    while len(queue):
        p = queue.popleft()
        for q in g[p]:
            if q == parents[p]:
                continue
            else:
                parents[q] = p
                children[p].append(q)
                order.append(q)
                queue.append(q)
    order = list(reversed(order))
    # print(order)
    for p in order:
        # 合計が合うかcheck
        count_child_p = [res[q] for q in children[p]]
        count_w = count_child_p.count("W")
        count_b = count_child_p.count("B")
        if count_w == count_b:
            if s[p] == "W":
                if res[parents[p]] == "B":
                    return "-1"
                res[parents[p]] = "W"
            else:
                if res[parents[p]] == "W":
                    return "-1"
                res[parents[p]] = "B"
        elif count_w > count_b:
            if s[p] == "B":
                return "-1"
        elif count_w < count_b:
            if s[p] == "W":
                return "-1"
        # ここまでで決まってないなら親に合わせる
        if res[p] == "":
            if p != 0:
                res[p] = s[parents[p]]
            else:
                res[p] = "B"
    # print(res)
    return "".join(res)


def solve(t, case_list):
    res = [solve_sub(n, ab_list, s) for n, ab_list, s in case_list]
    return res


def main():
    t = int(input())
    case_list = []
    for _ in range(t):
        n = int(input())
        ab_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
        s = input()
        case_list.append((n, ab_list, s))
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve(2, [
        (4, [(1, 2), (1, 3), (1, 4)], "BWWW"),
        (4, [(1, 2), (1, 3), (1, 4)], "BBWW")
    ]) == ["WBBB", "-1"]


if __name__ == "__main__":
    test()
    main()
