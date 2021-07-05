def solve(n, a, b):
    if a + b > n + 1:
        return "-1"
    elif a * b < n:
        return "-1"
    else:
        res_list = []
        # initial
        for i in range(b, 0, -1):
            res_list.append(i)
        c = b
        if a > 1:
            q = (n - b) // (a - 1)
            r = (n - b) % (a - 1)
            for j in range(a - 1):
                d = q
                if j < r:
                    d += 1
                for i in range(c + d, c, -1):
                    res_list.append(i)
                c += d
        # print(res_list)
        return " ".join([str(r) for r in res_list])


def main():
    n, a, b = map(int, input().split())
    res = solve(n, a, b)
    print(res)


def test():
    assert solve(5, 3, 2) == "2 1 4 3 5"
    assert solve(7, 7, 1) == "1 2 3 4 5 6 7"
    assert solve(300000, 300000, 300000) == "-1"


if __name__ == "__main__":
    test()
    main()
