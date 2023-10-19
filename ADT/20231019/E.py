def solve(n, a_list):
    odd = []
    even = []
    for a in a_list:
        if a % 2 == 1:
            odd.append(a)
        else:
            even.append(a)
    res = -1
    odd_s = list(sorted(odd))
    even_s = list(sorted(even))
    if len(odd_s) >= 2:
        res = max(res, odd_s[-1] + odd_s[-2])
    if len(even_s) >= 2:
        res = max(res, even_s[-1] + even_s[-2])
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [2, 3, 4]) == 6
    assert solve(2, [1, 0]) == -1


if __name__ == "__main__":
    test()
    main()
