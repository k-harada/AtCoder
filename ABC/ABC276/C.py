def solve(n, p_list):
    add = []
    for i in range(n - 1, 0, -1):
        add.append(p_list[i])
        if p_list[i - 1] > p_list[i]:
            d = p_list[i - 1]
            add_s = list(sorted(add))
            k = -1
            for j, a in enumerate(add_s):
                if a > d:
                    k = j - 1
                    break
            if k == -1:
                k = len(add_s) - 1
            # print(i, k, add_s)
            res = p_list[:(i - 1)] + [
                add_s[k]
            ] + list(sorted([p_list[i - 1]] + add_s[:k] + add_s[(k + 1):], reverse=True))
            break
    res_str = " ".join([str(r) for r in res])
    # print(res)
    return res_str


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    print(res)


def test():
    assert solve(3, [3, 1, 2]) == "2 3 1"
    assert solve(10, [9, 8, 6, 5, 10, 3, 1, 2, 4, 7]) == "9 8 6 5 10 2 7 4 3 1"


if __name__ == "__main__":
    test()
    main()
