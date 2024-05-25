def solve(n, s):
    res = 0
    count = [0] * 10
    for c in s:
        count[int(c)] += 1
    for i in range(10000000):
        q = str(i ** 2)
        if len(q) > n:
            break
        count_ = [0] * 10
        count_[0] += n - len(q)
        for c in q:
            count_[int(c)] += 1
        if count == count_:
            res += 1
    return res


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(4, "4320") == 2
    assert solve(3, "010") == 2
    assert solve(13, "8694027811503") == 840


if __name__ == "__main__":
    test()
    main()
