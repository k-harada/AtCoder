def solve(n, x):
    res = "1"
    x_list = list('0' * (n - len(x)) + x)
    # minus 1
    for i in range(1, n + 1):
        if x_list[-i] == '0':
            x_list[-i] = '1'
        else:
            x_list[-i] = '0'
            break

    for m in range(n - 1, -1, -1):
        k = n - 1 - m
        if x_list[k] == '1':
            x_list[k] = '0'
            res += '1'
        else:
            for i in range(1, n):
                if x_list[-i] == '0':
                    x_list[-i] = '1'
                else:
                    x_list[-i] = '0'
                    break
            else:
                return res
            res += '0'
        # print(x10, res)
    # print(res)
    return res


def main():
    n = int(input())
    x = input()
    res = solve(n, x)
    print(res)


def test():
    assert solve(3, '1') == '1'
    assert solve(3, '10') == '10'
    assert solve(3, '11') == '100'
    assert solve(3, '100') == '101'
    assert solve(3, '101') == '11'
    assert solve(3, '110') == '110'
    assert solve(3, '111') == '111'
    assert solve(10, '10100011') == '1001001111'
    assert solve(1000000, '11111') == '1000000000000000000000000000000'
    # assert solve(1000000, '1' * 999999) == '10' + '1' * 999996 + '10'


if __name__ == "__main__":
    test()
    main()
