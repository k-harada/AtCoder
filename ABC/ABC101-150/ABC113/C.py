def solve(n, m, py_list):
    pyi_list = [(py[0], py[1], i) for i, py in enumerate(py_list)]
    pyi_list_s = sorted(pyi_list, key=lambda x: (x[0], x[1]))
    c = [0] * (n + 1)
    res = ["0"] * m
    for p, y, i in pyi_list_s:
        c[p] += 1
        r = str(1000000 + p)[1:] + str(1000000 + c[p])[1:]
        res[i] = r
    return res


def main():
    n, m = map(int, input().split())
    py_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, py_list)
    for r in res:
        print(r)


def test():
    assert solve(2, 3, [(1, 32), (2, 63), (1, 12)]) == ["000001000002", "000002000001", "000001000001"]
    assert solve(2, 3, [(2, 55), (2, 77), (2, 99)]) == ["000002000001", "000002000002", "000002000003"]


if __name__ == "__main__":
    test()
    main()
