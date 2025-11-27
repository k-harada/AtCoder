def solve(n, m, t, a_list, xy_list):
    st = t
    if m > 0:
        j = 0
        x, y = xy_list[0]
    else:
        x, y = n + 1, 0
    for i in range(1, n):
        if i == x:
            st += y
            j += 1
            if j < m:
                x, y = xy_list[j]
            else:
                x, y = n + 1, 0
        if st <= a_list[i - 1]:
            return "No"
        st -= a_list[i - 1]
        # print(st)
    return "Yes"


def main():
    n, m, t = map(int, input().split())
    a_list = list(map(int, input().split()))
    xy_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, t, a_list, xy_list)
    print(res)


def test():
    assert solve(4, 1, 10, [5, 7, 5], [(2, 10)]) == "Yes"
    assert solve(4, 1, 10, [10, 7, 5], [(2, 10)]) == "No"


if __name__ == "__main__":
    test()
    main()
