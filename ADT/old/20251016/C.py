def solve(n, p_list):
    res = 0
    q = n
    p_list_2 = [0, 0] + p_list
    while q != 1:
        q = p_list_2[q]
        res += 1
    return res


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    print(res)


def test():
    assert solve(3, [1, 2]) == 2
    assert solve(10, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9


if __name__ == "__main__":
    test()
    main()
