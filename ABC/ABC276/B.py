def solve(n, m, ab_list):
    g = [[] for _ in range(n + 1)]
    for a, b in ab_list:
        g[a].append(b)
        g[b].append(a)
    res = []
    for i in range(1, n + 1):
        r = [len(g[i])] + list(sorted(g[i]))
        res.append(" ".join([str(a) for a in r]))
    return res


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, ab_list)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
