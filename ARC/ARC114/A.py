def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solve(n, x_list):
    primes = [
        2, 3, 5, 7, 11,
        13, 17, 19, 23, 29,
        31, 37, 41, 43, 47
    ]
    used = [0] * 50
    res_base = 1
    # use primes
    for x in x_list:
        if x in primes:
            if used[x] == 0:
                used[x] = 1
                res_base *= x

    for i in sorted([1, 2, 3, 5, 7, 6, 10, 14, 15, 21, 35, 30, 42, 70, 105, 210]):
        res = res_base * i
        flag = True
        for x in x_list:
            if gcd(x, res) == 1:
                flag = False
        if flag:
            break
    return res


def main():
    n = int(input())
    x_list = list(map(int, input().split()))
    res = solve(n, x_list)
    print(res)


def test():
    assert solve(2, [4, 3]) == 6
    assert solve(1, [47]) == 47
    assert solve(7, [3, 4, 6, 7, 8, 9, 10]) == 42


if __name__ == "__main__":
    test()
    main()
