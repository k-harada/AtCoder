def solve_one(n, k, s):
    x_list = [-1]
    for i in range(n):
        if s[i % n] == "x":
            x_list.append(i)
    x_list.append(n)
    # print(x_list)
    add_max = 0
    for i, x in enumerate(x_list):
        if i + k + 1 < len(x_list):
            add = x_list[i + k + 1] - x - 1
        else:
            break
        add_max = max(add_max, add)
    return add_max


def solve(n, m, k, s):
    if m == 1:
        return solve_one(n, k, s)
    c = s.count("x")
    x_list = [-1]
    for i in range(2 * n):
        if s[i % n] == "x":
            x_list.append(i)
    x_list.append(2 * n)
    # print(x_list)
    res = 0
    for i, x in enumerate(x_list):
        if x >= n:
            break
        r = 0
        # この後のxの数
        d0 = c - i
        # 省略できる数
        if (k - d0) > 0:
            rep = min(m - 2, (k - d0) // c)
            r += n * rep
            d1 = k - d0 - rep * c
            if i + d0 + d1 + 1 < len(x_list):
                r += x_list[i + d0 + d1 + 1] - x - 1
            else:
                r += 2 * n - x - 1
        else:
            r += x_list[i + k + 1] - x - 1
        res = max(res, r)
    # print(res)
    return res


def main():
    n, m, k = map(int, input().split())
    s = input()
    res = solve(n, m, k, s)
    print(res)


def test():
    assert solve(10, 1, 2, "ooxxooooox") == 9
    assert solve(5, 3, 4, "oxxox") == 8
    assert solve(30, 1000000000, 9982443530, "oxoxooxoxoxooxoxooxxxoxxxooxox") == 19964887064


if __name__ == "__main__":
    test()
    main()
