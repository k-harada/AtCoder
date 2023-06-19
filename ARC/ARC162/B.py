def solve(n, p_list):
    q_list = p_list.copy()
    res = []
    x = 1
    c = 0
    while x <= n:
        i0 = 0
        for i in range(n):
            if q_list[i] == x:
                i0 = i
        if i0 == x - 1:
            x += 1
            continue
        if i0 == n - 1:
            i = n - 2
        else:
            i = i0
        r_list = q_list[:i] + q_list[i + 2:]
        s_list = [q_list[i], q_list[i + 1]]
        # print(i0, r_list, s_list)
        q_list = r_list[:(x - 1)] + s_list + r_list[(x - 1):]
        # print(q_list)
        res.append(f"{i + 1} {x - 1}")
        c += 1
        if c == 2001:
            return ["No"]
    # print(res)
    return ["Yes"] + [str(len(res))] + res


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    for r in res:
        print(r)


def test():
    assert solve(5, [1, 4, 2, 3, 5]) == ["Yes", "1", "3 1"]
    assert solve(2, [2, 1]) == ["No"]
    assert solve(4, [3, 4, 1, 2]) == ["Yes", "1", "3 0"]


if __name__ == "__main__":
    test()
    main()
