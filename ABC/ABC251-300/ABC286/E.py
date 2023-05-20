def solve(n, a_list, s, q, uv_list):
    large = 10 ** 12
    ex_large = 10 ** 15
    d = [[ex_large] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if s[i][j] == "Y":
                d[i][j] = large - a_list[j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    res = []
    for u, v in uv_list:
        d_uv = d[u - 1][v - 1]
        if d_uv == ex_large:
            res.append("Impossible")
        else:
            c = d_uv // large + 1
            z = c * large - d_uv + a_list[u - 1]
            res.append(f"{c} {z}")
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    s = [input() for _ in range(n)]
    q = int(int(input()))
    uv_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, a_list, s, q, uv_list)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
