def solve(n):
    mod3_cnt = [0] * 3
    for s in str(n):
        mod3_cnt[int(s) % 3] += 1
    mod3_all = n % 3

    if mod3_all == 0:
        return 0
    elif mod3_all == 1:
        if mod3_cnt[1] > 0:
            if len(str(n)) > 1:
                return 1
            else:
                return -1
        elif mod3_cnt[2] > 1:
            if len(str(n)) > 2:
                return 2
            else:
                return -1
        else:
            return -1
    else:
        if mod3_cnt[2] > 0:
            if len(str(n)) > 1:
                return 1
            else:
                return -1
        elif mod3_cnt[1] > 1:
            if len(str(n)) > 2:
                return 2
            else:
                return -1
        else:
            return -1


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(35) == 1
    assert solve(369) == 0
    assert solve(6227384) == 1
    assert solve(11) == -1


if __name__ == "__main__":
    test()
    main()
