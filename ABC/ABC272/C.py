def solve(n, a_list):
    even = []
    odd = []
    for a in a_list:
        if a % 2 == 0:
            even.append(a)
        else:
            odd.append(a)
    even = list(sorted(even))
    odd = list(sorted(odd))
    res = -1
    if len(even) >= 2:
        res = max(res, even[-1] + even[-2])
    if len(odd) >= 2:
        res = max(res, odd[-1] + odd[-2])
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
