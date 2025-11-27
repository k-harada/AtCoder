def solve(n, m, k, car_list):
    res = 0
    for i in range(2 ** n):
        j = 2 ** n + i
        re = 1
        for c, a_list, r in car_list:
            x = 0
            for a in a_list:
                if (j >> (a - 1)) % 2:
                    x += 1
            if (x >= k and r == "x") or (x < k and r == "o"):
                re = 0
                break
        # print(i, x)
        res += re
    # print(res)
    return res


def main():
    n, m, k = map(int, input().split())
    car_list = []
    for _ in range(m):
        car = input().split()
        c = int(car[0])
        r = car[-1]
        a = [int(x) for x in car[1:-1]]
        car_list.append((c, a, r))
    res = solve(n, m, k, car_list)
    print(res)


def test():
    assert solve(3, 2, 2, [(3, [1, 2, 3], "o"), (2, [2, 3], "x")]) == 2
    assert solve(4, 5, 3, [
        (3, [1, 2, 3], "o"),
        (3, [2, 3, 4], "o"),
        (3, [3, 4, 1], "o"),
        (3, [4, 1, 2], "o"),
        (4, [1, 2, 3, 4], "x")
    ]) == 0
    assert solve(11, 4, 9, [
        (10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "o"),
        (11, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "o"),
        (10, [11, 10, 9, 8, 7, 6, 5, 4, 3, 2], "x"),
        (10, [11, 9, 1, 4, 3, 7, 5, 6, 2, 10], "x")
    ]) == 8


if __name__ == "__main__":
    test()
    main()
