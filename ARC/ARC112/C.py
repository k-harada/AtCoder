import numpy as np


def solve(n, p_list):

    children_list = [[] for _ in range(n + 1)]
    for i, p in enumerate(p_list):
        children_list[p].append(i + 2)
    collect_res_list = [(-1, -1, -1)] * (n + 1)

    for a in range(n, 0, -1):
        if len(children_list[a]) == 0:
            collect_res_list[a] = (1, 0, 1)
        else:
            s = 1
            t = 0
            res_list = [collect_res_list[c] for c in children_list[a]]
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

    d = collect_res_list[1]
    return d[0]


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    print(res)


def test():
    assert solve(10, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10
    assert solve(5, [1, 2, 3, 1]) == 2
    assert solve(10, [1, 1, 3, 1, 3, 6, 7, 6, 6]) == 5
    for _ in range(100):
        n = 5
        p_list = [np.random.choice(p) + 1 for p in range(1, n)]
        q = solve(n, p_list)
        print(q)
    print("done")


if __name__ == "__main__":
    # test()
    main()
