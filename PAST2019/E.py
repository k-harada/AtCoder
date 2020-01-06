def solve(n, q, s_list):

    g = {i + 1: {} for i in range(n)}
    for i in range(q):
        s = s_list[i]
        if s[0] == "1":
            _, a, b = map(int, s.split())
            g[a][b] = 1
        elif s[0] == "2":
            _, a = map(int, s.split())
            for b in range(n):
                if a in g[b + 1].keys():
                    g[a][b + 1] = 1
        else:
            _, a = map(int, s.split())
            do_list = []
            for b in g[a].keys():
                for c in g[b].keys():
                    if c != a:
                        do_list.append(c)
            for c in do_list:
                g[a][c] = 1

    res_list = [["N"] * n for _ in range(n)]
    for a in g.keys():
        for b in g[a].keys():
            res_list[a - 1][b - 1] = "Y"
    res = ["".join(res_list[i]) for i in range(n)]
    return res


def main():
    n, q = map(int, input().split())
    s_list = [""] * q
    for i in range(q):
        s = input()
        s_list[i] = s
    res = solve(n, q, s_list)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
