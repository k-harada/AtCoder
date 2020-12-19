def solve(n, a_list):
    a_list_s = list(sorted(a_list))
    res = 0
    positive = 0
    negative = n - 1
    for i in range(n):
        a = a_list_s[i]
        res += positive * a - negative * a
        positive += 1
        negative -= 1
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [5, 1, 2]) == 8
    assert solve(5, [31, 41, 59, 26, 53]) == 176


if __name__ == "__main__":
    test()
    main()
