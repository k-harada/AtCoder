def solve(s_list):
    a = 10
    b = 0
    c = 10
    d = 0

    for i in range(10):
        for j in range(10):
            if s_list[i][j] == "#":
                a = min(i + 1, a)
                b = max(i + 1, b)
                c = min(j + 1, c)
                d = max(j + 1, d)

    return [f"{a} {b}", f"{c} {d}"]


def main():
    s_list = [input() for _ in range(10)]
    res = solve(s_list)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
