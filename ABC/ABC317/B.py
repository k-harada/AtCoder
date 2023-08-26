def solve(n, a_list):
    a_list_s = list(sorted(a_list))
    for i in range(n - 1):
        if a_list_s[i] + 1 < a_list_s[i + 1]:
            return a_list_s[i] + 1
    return 0


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [2, 3, 5]) == 4
    assert solve(8, [3, 1, 4, 5, 9, 2, 6, 8]) == 7
    assert solve(16, [
        152, 153, 154, 147, 148, 149, 158, 159,
        160, 155, 156, 157, 144, 145, 146, 150
    ]) == 151


if __name__ == "__main__":
    test()
    main()
