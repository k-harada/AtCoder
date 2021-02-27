def solve(n):
    res_list = []
    for i in range(2, n):
        d = i * i
        if d > n:
            break
        while d <= n:
            res_list.append(d)
            d *= i
    res = n - len(set(res_list))
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(8) == 6
    assert solve(100000) == 99634


if __name__ == "__main__":
    test()
    main()
