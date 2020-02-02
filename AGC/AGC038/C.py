LARGE = 998244353


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def solve_c_greedy(n, a_list):
    res = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            res += lcm(a_list[i], a_list[j])
            res %= LARGE

    return res


def main_greed():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve_c_greedy(n, a_list)
    print(res)


if __name__ == "__main__":
    main_greed()
