def solve(n):
    cnt_dict = dict()
    for k in range(11, 100):
        if k % 10 != 0:
            cnt_dict[str(k)] = 0
    for i in range(1, n + 1):
        if i % 10 != 0:
            cnt_dict[str(i)[0] + str(i)[-1]] += 1
    res = 0  # 0 is ignored
    for k in range(11, 100):
        if k % 10 != 0:
            res += cnt_dict[str(k)] * cnt_dict[str(k)[1] + str(k)[0]]
    # print(res)
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(25) == 17
    assert solve(1) == 1
    assert solve(100) == 108
    assert solve(2020) == 40812
    assert solve(200000) == 400000008


if __name__ == "__main__":
    test()
    main()
