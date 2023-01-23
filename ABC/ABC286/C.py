def solve(n, a, b, s):
    ss = s + s
    k = n // 2
    cost_array = [0] * n
    for i in range(n):
        cost_array[i] += i * a
        for j in range(k):
            if ss[i + j] != ss[n - 1 + i - j]:
                cost_array[i] += b
    return min(cost_array)


def main():
    n, a, b = map(int, input().split())
    s = input()
    res = solve(n, a, b, s)
    print(res)


def test():
    assert solve(5, 1, 2, "rrefa") == 3
    assert solve(8, 1000000000, 1000000000, "bcdfcgaa") == 4000000000


if __name__ == "__main__":
    test()
    main()
