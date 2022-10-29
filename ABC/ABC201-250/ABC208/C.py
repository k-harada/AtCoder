def solve(n, k, a_list):
    base = k // n
    m = k % n
    a_list_id = [(a, i) for i, a in enumerate(a_list)]
    a_list_id_s = list(sorted(a_list_id, key=lambda x: x[0]))
    res = [base] * n
    for j in range(m):
        _, i = a_list_id_s[j]
        res[i] += 1
    return res


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    for r in res:
        print(r)


def test():
    assert solve(2, 7, [1, 8]) == [4, 3]
    assert solve(1, 3, [33]) == [3]
    assert solve(7, 1000000000000, [99, 8, 2, 4, 43, 5, 3]) == [
        142857142857, 142857142857, 142857142858, 142857142857, 142857142857, 142857142857, 142857142857
    ]


if __name__ == "__main__":
    test()
    main()
