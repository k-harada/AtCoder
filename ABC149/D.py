def solve(n, k, r, s, p, t):
    res = 0
    u_list = [""] * n
    for i in range(k):
        if t[i] == "r":
            u_list[i] = "p"
            res += p
        elif t[i] == "s":
            u_list[i] = "r"
            res += r
        else:
            u_list[i] = "s"
            res += s

    for i in range(k, n):
        if t[i] == "r":
            if u_list[i - k] != "p":
                u_list[i] = "p"
                res += p
            else:
                u_list[i] = "x"
        elif t[i] == "s":
            if u_list[i - k] != "r":
                u_list[i] = "r"
                res += r
            else:
                u_list[i] = "x"
        else:
            if u_list[i - k] != "s":
                u_list[i] = "s"
                res += s
            else:
                u_list[i] = "x"
    return res


def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    res = solve(n, k, r, s, p, t)
    print(res)


def test():
    assert solve(5, 2, 8, 7, 6, "rsrpr") == 27
    assert solve(7, 1, 100, 10, 1, "ssssppr") == 211
    assert solve(30, 5, 325, 234, 123, "rspsspspsrpspsppprpsprpssprpsr") == 4996


if __name__ == "__main__":
    test()
    main()
