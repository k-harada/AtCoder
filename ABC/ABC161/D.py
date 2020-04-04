def solve(k):

    if k <= 9:
        return k
    cnt = 9
    tmp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tmp_new = []
    while True:
        for p in tmp:
            m = p % 10
            if m == 0:
                tmp_new.append(p * 10)
                cnt += 1
                if cnt == k:
                    return tmp_new[-1]
                tmp_new.append(p * 10 + 1)
                cnt += 1
                if cnt == k:
                    return tmp_new[-1]
            elif m == 9:
                tmp_new.append(p * 10 + 8)
                cnt += 1
                if cnt == k:
                    return tmp_new[-1]
                tmp_new.append(p * 10 + 9)
                cnt += 1
                if cnt == k:
                    return tmp_new[-1]
            else:
                tmp_new.append(p * 10 + m - 1)
                cnt += 1
                if cnt == k:
                    return tmp_new[-1]
                tmp_new.append(p * 10 + m)
                cnt += 1
                if cnt == k:
                    return tmp_new[-1]
                tmp_new.append(p * 10 + m + 1)
                cnt += 1
                if cnt == k:
                    return tmp_new[-1]
        tmp = tmp_new
        tmp_new = []

    return 0


def main():
    k = int(input())
    res = solve(k)
    print(res)


def test():
    assert solve(15) == 23
    assert solve(1) == 1
    assert solve(13) == 21
    assert solve(100000) == 3234566667


if __name__ == "__main__":
    test()
    main()
