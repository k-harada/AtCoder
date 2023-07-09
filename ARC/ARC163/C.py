def solve_sub(n):
    for i in range(n):
        if i * (i + 1) == n:
            return [2] + [2 * p for p in solve_sub(n - 1)]
    r = [n]
    for i in range(1, n):
        r.append(i * (i + 1))
    return r


def solve(t, case_list):
    res = []
    for n in case_list:
        if n == 2:
            res.append("No")
        elif n == 1:
            res.append("Yes")
            res.append("1")
        else:
            res.append("Yes")
            res.append(" ".join([str(p) for p in solve_sub(n)]))

    return res


def main():
    t = int(input())
    case_list = [int(input()) for _ in range(t)]
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve(2, [3, 5]) == ['Yes', '3 2 6', 'Yes', '5 2 6 12 20']


if __name__ == "__main__":
    test()
    main()
