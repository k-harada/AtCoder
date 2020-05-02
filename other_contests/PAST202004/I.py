def solve(n, a_list):
    res_list = [0] * (2 ** n)
    a_list_s = [[] for i in range(n)]
    for i in range(2 ** n):
        a_list_s[0].append(i)
    for i in range(1, n):
        for j in range(2 ** (n - i)):
            if a_list[a_list_s[i - 1][2 * j]] > a_list[a_list_s[i - 1][2 * j + 1]]:
                a_list_s[i].append(a_list_s[i - 1][2 * j])
                res_list[a_list_s[i - 1][2 * j + 1]] = i
            else:
                a_list_s[i].append(a_list_s[i - 1][2 * j + 1])
                res_list[a_list_s[i - 1][2 * j]] = i
    for a in a_list_s[-1]:
        res_list[a] = n
    return res_list


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    for r in res:
        print(r)


def test():
    assert solve(2, [2, 4, 3, 1]) == [1, 2, 2, 1]
    assert solve(1, [2, 1]) == [1, 1]
    assert solve(3, [4, 7, 5, 1, 6, 3, 2, 8]) == [1, 3, 2, 1, 2, 1, 1, 3]


if __name__ == "__main__":
    test()
    main()
