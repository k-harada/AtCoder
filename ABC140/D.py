def solve_d(n, k, s):
    res = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            res += 1
    d = n - 1 - res
    if 2 * k > d:
        return n - 1
    else:
        return res + 2 * k


def main():
    n, k = map(int, input().split())
    s = list(input())
    print(solve_d(n, k, s))


if __name__ == "__main__":
    main()
