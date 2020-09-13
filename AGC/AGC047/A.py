def solve(n, a_str_list):

    count_25 = [[0] * 19 for _ in range(19)]
    for i in range(n):
        a_str = a_str_list[i]
        if "." in a_str:
            a_str_a, a_str_b = a_str.split(".")
            a_int = int(a_str_a + a_str_b + "0" * (9 - len(a_str_b)))
        else:
            a_int = int(a_str) * 1000000000
        count_2 = 0
        count_5 = 0
        while a_int % 2 == 0:
            a_int = a_int // 2
            count_2 += 1
        while a_int % 5 == 0:
            a_int = a_int // 5
            count_5 += 1
        count_2 = min(count_2, 18)
        count_5 = min(count_5, 18)
        # print(a_str, count_2, count_5)
        count_25[count_2][count_5] += 1
    # print(count_25)

    res = 0
    for i0 in range(19):
        for j0 in range(19):
            for i1 in range(19):
                for j1 in range(19):
                    if count_25[i0][j0] * count_25[i1][j1] and i0 + i1 >= 18 and j0 + j1 >= 18:
                        # print(i0, j0, i1, j1)
                        if i0 == i1 and j0 == j1:
                            res += (count_25[i0][j0] - 1) * count_25[i0][j0]
                        elif i0 == i1:
                            res += count_25[i0][j0] * count_25[i0][j1]
                        elif j0 == j1:
                            res += count_25[i0][j0] * count_25[i1][j0]
                        else:
                            res += count_25[i0][j0] * count_25[i1][j1]
    # print(res)
    return res // 2


def main():
    n = int(input())
    a_str_list = [input() for _ in range(n)]
    res = solve(n, a_str_list)
    print(res)


def test():
    assert solve(5, ["7.5", "2.4", "17.000000001", "17", "16.000000000"]) == 3
    assert solve(11, [
        "0.9", "1", "1", "1.25", "2.30000", "5", "70", "0.000000001", "9999.999999999", "0.999999999", "1.000000001"
    ]) == 8


if __name__ == "__main__":
    test()
    main()
