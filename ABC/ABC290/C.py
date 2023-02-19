def solve(n, k, a_list):
    a_set = list(sorted(list(set(a_list))))
    m = min(len(a_set), k)
    for i in range(m):
        if a_set[i] != i:
            return i
    return m


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
