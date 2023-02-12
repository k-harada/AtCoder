def solve_sub_small(n, k):
    a = []
    if n == 2:
        a = [2, 1]
        return a[k - 1]
    elif n == 3:
        a = [2, 3, 1]
        return a[k - 1]
    elif n == 4:
        a = [2, 1, 4, 3]
        return a[k - 1]
    elif n == 5:
        a = [2, 4, 1, 5, 3]
        return a[k - 1]
    elif n == 6:
        a = [2, 1, 3, 4, 6, 5]
        return a[k - 1]
    elif n == 7:
        a = [2, 3, 1, 4, 6, 7, 5]
        return a[k - 1]
    elif n == 8:
        a = [2, 1, 4, 3, 6, 5, 8, 7]
        return a[k - 1]


def solve_sub(n, k):
    if n <= 8:
        return solve_sub_small(n, k)
    else:
        # n に一番近い2のべき
        m = 1
        while m * 2 <= n:
            m *= 2
        if n == m:
            if k % 2 == 1:
                return k + 1
            else:
                return k - 1
        elif n == m + 1:
            if k == 1:
                return 2
            elif k == n - 1:
                return n
            elif k % 2 == 1:
                return k - 2
            else:
                return k + 2
        else:
            if k <= n - m:
                # print(n - m, k)
                return solve_sub(n - m, k)
            elif k >= m + 1:
                # print(n - m, k - m)
                return m + solve_sub(n - m, k - m)
            else:
                return k


def solve(t, case_list):
    res = [solve_sub(n, k) for n, k in case_list]
    return res


def main():
    t = int(input())
    case_list = [tuple(map(int, input().split())) for _ in range(t)]
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    print(solve(6, [(6, i + 1) for i in range(6)]))
    print(solve(7, [(7, i + 1) for i in range(7)]))
    print(solve(8, [(8, i + 1) for i in range(8)]))
    print(solve(9, [(9, i + 1) for i in range(9)]))
    print(solve(10, [(10, i + 1) for i in range(10)]))
    print(solve(11, [(11, i + 1) for i in range(11)]))
    print(solve(12, [(12, i + 1) for i in range(12)]))
    print(solve(13, [(13, i + 1) for i in range(13)]))
    print(solve(14, [(14, i + 1) for i in range(14)]))
    print(solve(15, [(15, i + 1) for i in range(15)]))


if __name__ == "__main__":
    # test()
    main()
