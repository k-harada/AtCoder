import sys


def solve(n, p_list):
    children_list = [[] for _ in range(n + 1)]
    for i, p in enumerate(p_list):
        children_list[p].append(i + 2)
    collect_res_list = [(-1, -1, -1)] * (n + 1)

    def collect(a):
        if collect_res_list[a] != (-1, -1, -1):
            return collect_res_list[a]
        if len(children_list[a]) == 0:
            collect_res_list[a] = (1, 0, 1)
            return collect_res_list[a]
        else:
            s = 1
            t = 0
            res_list = [collect(c) for c in children_list[a]]
            res_list_0 = [(res[0], res[1]) for res in res_list if res[2] == 0]
            res_list_1 = [(res[0], res[1]) for res in res_list if res[2] == 1]
            for ss, tt in res_list_0:
                if ss < tt:
                    t += tt
                    s += ss
                else:
                    if len(res_list_1) % 2 == 0:
                        t += tt
                        s += ss
                    else:
                        t += ss
                        s += tt
            res_list_1s = sorted(res_list_1, key=lambda x: x[0] - x[1])
            for j, res in enumerate(res_list_1s):
                if j % 2 == 0:
                    s += res[0]
                    t += res[1]
                else:
                    s += res[1]
                    t += res[0]
            collect_res_list[a] = (s, t, (len(res_list_1) + 1) % 2)
            return collect_res_list[a]

    d = collect(1)
    # print(children_list)
    # print(collect_res_list)
    return d[0]


def main():
    sys.setrecursionlimit(10 ** 7 + 7)
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    print(res)


def test():
    sys.setrecursionlimit(10 ** 7 + 7)
    assert solve(10, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10
    assert solve(5, [1, 2, 3, 1]) == 2
    assert solve(10, [1, 1, 3, 1, 3, 6, 7, 6, 6]) == 5
    c = solve(10 ** 5 + 1, [i + 1 for i in range(10 ** 5)])


if __name__ == "__main__":
    test()
    main()
