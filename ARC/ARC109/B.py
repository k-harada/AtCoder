def solve(n):
    left = 0
    right = n + 1

    while left + 1 < right:
        mid = (left + right) // 2

        if mid * (mid + 1) // 2 > n + 1:
            right = mid
        else:
            left = mid
    return n + 1 - left


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(4) == 3
    assert solve(109109109109109109) == 109109108641970782


if __name__ == "__main__":
    test()
    main()
