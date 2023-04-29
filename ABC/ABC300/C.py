def solve(h, w, c):
    res = [0] * min(h, w)
    d = [[c[i][j] for j in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            if d[i][j] == "#":
                le = 1
                d[i][j] = "."
                while d[i + le][j + le] == "#":
                    d[i + le][j + le] = "."
                    le += 1
                    if i + le == h or j + le == w:
                        break
                res[le // 2 - 1] += 1
                for m in range(le):
                    d[i + le - 1 - m][j + m] = "."

    return " ".join([str(r) for r in res])


def main():
    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    res = solve(h, w, c)
    print(res)


if __name__ == "__main__":
    main()
