def solve(n, tlr_list):
    lr_list = []
    for t, l, r in tlr_list:
        if t == 1:
            lr_list.append((l, r))
        elif t == 2:
            lr_list.append((l, r - 0.1))
        elif t == 3:
            lr_list.append((l + 0.1, r))
        else:
            lr_list.append((l + 0.1, r - 0.1))
    lr_list_s = list(sorted(lr_list, key=lambda x: x[0]))
    # print(lr_list_s)
    res = 0
    for i in range(n - 1):
        right = lr_list_s[i][1]
        for j in range(i + 1, n):
            left = lr_list_s[j][0]
            if left <= right:
                # print(i, j)
                res += 1
    # print(res)
    return res


def main():
    n = int(input())
    tlr_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, tlr_list)
    print(res)


def test():
    assert solve(3, [(1, 1, 2), (2, 2, 3), (3, 2, 4)]) == 2


if __name__ == "__main__":
    test()
    main()
