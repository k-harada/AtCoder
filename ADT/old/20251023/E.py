def solve(n, k, a_list):
    a_list_su = list(sorted(list(set(a_list))))
    r = min(k, len(a_list_su))
    for i in range(r):
        if a_list_su[i] != i:
            return i
    return r


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(7, 3, [2, 0, 2, 3, 2, 1, 9]) == 3


if __name__ == "__main__":
    test()
    main()
