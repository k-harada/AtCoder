def solve(n, a_list):
    if n == 1:
        return a_list[0]
    res = 0
    for i in range(n):
        j = i
        k = i
        while a_list[j] >= a_list[i]:
            j -= 1
            if j < 0:
                break
        while a_list[k] >= a_list[i]:
            k += 1
            if k >= n:
                break
        res = max(res, a_list[i] * (k - j - 1))
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(6, [2, 4, 4, 9, 4, 9]) == 20
    assert solve(6, [200, 4, 4, 9, 4, 9]) == 200


def test_large():
    assert solve(10000, [1] * 10000) == 10000


if __name__ == "__main__":
    test()
    main()
