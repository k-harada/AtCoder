def solve(s):
    res = 0
    count_array = [0] * 1024
    count_array[0] = 1
    v = 0
    for i, c in enumerate(s):
        w = int(c)
        v ^= 2 ** w
        count_array[v] += 1
    # print(count_array)
    for x in count_array:
        res += x * (x - 1) // 2
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("20230322") == 4
    assert solve("0112223333444445555556666666777777778888888889999999999") == 185
    assert solve("3141592653589793238462643383279502884197169399375105820974944") == 9


if __name__ == "__main__":
    test()
    main()
