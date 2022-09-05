def solve(n, a_list):
    a = min(a_list)
    big_list = list(sorted(a_list, reverse=True))
    res = 0
    small_list = []
    while True:
        for b in big_list:
            d = b % a
            if d != 0:
                small_list.append(d)
                if d < a:
                    a = d
            res += 1
        if len(small_list) == 1:
            break
        if len(small_list) == 0:
            res -= 1
            break
        big_list = list(sorted(small_list, reverse=True))
        small_list = []
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [2, 3, 6]) == 3
    assert solve(6, [1232, 452, 23491, 34099, 57341, 21488]) == 12


def test_large():
    print(solve(200000, list(range(1000000009, 2000000009, 5000))))


if __name__ == "__main__":
    test()
    # test_large()
    main()
