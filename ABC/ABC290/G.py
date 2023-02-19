def solve_sub(d, k, x):
    size_list = [1]
    for _ in range(d):
        size_list.append(size_list[-1] * k + 1)
    # print(size_list)
    if x == size_list[-1]:
        return 0
    e = d
    for i in range(d + 1):
        if size_list[i] >= x:
            e = i
            break
    if e == d:
        res_a = 0
    else:
        res_a = 1
    y = size_list[e]
    for j in range(e - 1, -1, -1):
        q = (y - x) // size_list[j]
        y -= size_list[j] * q
        res_a += q

    res_b = 0
    y = size_list[-1]
    for j in range(d - 1, -1, -1):
        q = (y - x) // size_list[j]
        y -= size_list[j] * q
        res_b += q
    return min(res_a, res_b)


def solve(t, case_list):
    return [solve_sub(d, k, x) for d, k, x in case_list]


def main():
    t = int(input())
    case_list = [tuple(map(int, input().split())) for _ in range(t)]
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve(11, [
        (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 2, 5), (2, 2, 6), (2, 2, 7),
        (1, 999999999999999999, 1), (1, 999999999999999999, 2), (1, 999999999999999999, 999999999999999999),
        (1, 999999999999999999, 1000000000000000000)
    ]) == [1, 2, 1, 1, 2, 1, 0, 1, 999999999999999998, 1, 0]


if __name__ == "__main__":
    test()
    main()
