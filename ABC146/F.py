from collections import defaultdict


def solve(n, m, s):
    i = n
    res_list = []
    while i > 0:
        flag = True
        for j in range(min(i, m), 0, -1):
            if s[i - j] == "0":
                res_list.append(j)
                i -= j
                flag = False
                break
        if flag:
            return [-1]
    return list(reversed(res_list))


def main():
    n, m = map(int, input().split())
    s = input()
    res_list = solve(n, m, s)
    print(*res_list)


def test():
    assert solve(9, 3, "0001000100") == [1, 3, 2, 3]
    assert solve(5, 4, "011110") == [-1]
    assert solve(6, 6, "0101010") == [6]


if __name__ == "__main__":
    test()
    main()
