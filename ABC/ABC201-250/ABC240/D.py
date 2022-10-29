def solve(n, a_list):
    r = 0
    res = []
    ac_list = []
    a_before = 0
    a_con = 0
    for i, a in enumerate(a_list):
        if a == a_before:
            a_con += 1
            if a_con == a:
                if len(ac_list) > 0:
                    a_before, a_con = ac_list.pop()
                else:
                    a_before, a_con = 0, 0
                r -= a - 1
                res.append(r)
            else:
                r += 1
                res.append(r)
        else:
            ac_list.append((a_before, a_con))
            a_before = a
            a_con = 1
            r += 1
            res.append(r)

    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    for r in res:
        print(r)


def test():
    assert solve(5, [3, 2, 3, 2, 2]) == [1, 2, 3, 4, 3]
    assert solve(10, [2, 3, 2, 3, 3, 3, 2, 3, 3, 2]) == [1, 2, 3, 4, 5, 3, 2, 3, 1, 0]


if __name__ == "__main__":
    test()
    main()
