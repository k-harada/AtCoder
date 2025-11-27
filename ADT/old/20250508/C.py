def solve(n, a_list):
    m = max(a_list)
    r_list = []
    for a in a_list:
        if a < m:
            r_list.append(a)
    return max(r_list)


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(5, [2, 1, 3, 3, 2]) == 2
    assert solve(4, [4, 3, 2, 1]) == 3
    assert solve(8, [22, 22, 18, 16, 22, 18, 18, 22]) == 18


if __name__ == "__main__":
    test()
    main()
