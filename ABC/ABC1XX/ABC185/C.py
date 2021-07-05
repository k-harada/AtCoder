def solve(ll):
    res = 1
    for i in range(1, 12):
        res *= ll - i
    for i in range(1, 12):
        res //= i
    return res


def main():
    ll = int(input())
    res = solve(ll)
    print(res)


def test():
    assert solve(12) == 1
    assert solve(13) == 12
    assert solve(17) == 4368


if __name__ == "__main__":
    test()
    main()
