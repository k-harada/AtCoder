def solve(n):
    v_dict = dict()
    v_dict[n] = 0
    queue = [n]
    while len(queue) > 0:
        p = queue.pop()
        q = p // 2
        r = p // 3
        if q > 0:
            if q not in v_dict.keys():
                v_dict[q] = 0
                queue.append(q)
        if r > 0:
            if r not in v_dict.keys():
                v_dict[r] = 0
                queue.append(r)
    v_dict[0] = 1
    for p in list(sorted(list(v_dict.keys()))):
        if p == 0:
            continue
        q = p // 2
        r = p // 3
        v_dict[p] = v_dict[q] + v_dict[r]

    return v_dict[n]


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(2) == 3
    assert solve(0) == 1
    assert solve(100) == 55


def test_large():
    print(solve(10 ** 18))


if __name__ == "__main__":
    test()
    # test_large()
    main()
