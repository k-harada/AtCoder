def solve(n):
    res_list = []
    j_list = [j for j in range(9, 0, -1) if n % j == 0]
    for i in range(n + 1):
        res = 0
        for j in j_list:
            if n % j == 0:
                k = n // j
                if i % k == 0:
                    res = j
        if res > 0:
            res_list.append(str(res))
        else:
            res_list.append("-")

    return "".join(res_list)


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(12) == "1-643-2-346-1"
    assert solve(7) == "17777771"
    assert solve(1) == "11"


if __name__ == "__main__":
    test()
    main()
