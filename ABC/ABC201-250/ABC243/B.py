def solve(n, a_list, b_list):
    hit = 0
    for i in range(n):
        if a_list[i] == b_list[i]:
            hit += 1
    a_list_s = list(sorted(a_list))
    b_list_s = list(sorted(b_list))

    i = 0
    j = 0
    blow = - hit
    while i < n and j < n:
        if a_list_s[i] == b_list_s[j]:
            i += 1
            j += 1
            blow += 1
        elif a_list_s[i] > b_list_s[j]:
            j += 1
        else:
            i += 1

    return [hit, blow]


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, a_list, b_list)
    for r in res:
        print(r)


def test():
    assert solve(4, [1, 3, 5, 2], [2, 3, 1, 4]) == [1, 2]
    assert solve(3, [1, 2, 3], [4, 5, 6]) == [0, 0]
    assert solve(7, [4, 8, 1, 7, 9, 5, 6], [3, 5, 1, 7, 8, 2, 6]) == [3, 2]


if __name__ == "__main__":
    test()
    main()
