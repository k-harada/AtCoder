def solve(q, abc_list):
    res_list = [0] * q
    for i in range(q):
        a, b, c, d = abc_list[i]
        a, b, c, d = a - 1, b - 1, c - 1, d - 1
        a2, b2, c2, d2 = a, b, c, d
        k1 = 29
        flag = 0
        while k1 >= 0:
            if 3 ** k1 <= a2 < 2 * 3 ** k1 and 3 ** k1 <= c2 < 2 * 3 ** k1:
                if min(b2, d2) < 3 ** k1 and 2 * 3 ** k1 <= max(b2, d2):
                    flag = 1
                    break
            elif 3 ** k1 <= b2 < 2 * 3 ** k1 and 3 ** k1 <= d2 < 2 * 3 ** k1:
                if min(a2, c2) < 3 ** k1 and 2 * 3 ** k1 <= max(a2, c2):
                    flag = 2
                    break
            elif a2 // (3 ** k1) != c2 // (3 ** k1) and a2 // (3 ** k1) != c2 // (3 ** k1):
                k1 = -1
                break
            a2, b2, c2, d2 = a2 % 3, b2 % 3, c2 % 3, d2 % 3
            k1 -= 1

        add = 0

        if flag == 1:
            add = min(a2 - 3 ** k1 + 1 + c2 - 3 ** k1 + 1, 2 * (3 ** k1) - a2 + 2 * (3 ** k1) - c2)
        elif flag == 2:
            add = min(b2 - 3 ** k1 + 1 + d2 - 3 ** k1 + 1, 2 * (3 ** k1) - b2 + 2 * (3 ** k1) - d2)
        res_list[i] = abs(a - c) + abs(b - d) + add
    return res_list


def main():
    q = int(input())
    abc_list = [list(map(int, input().split())) for _ in range(q)]
    res_list = solve(q, abc_list)
    for r in res_list:
        print(r)


def test():
    assert solve(2, [[4, 2, 7, 4], [9, 9, 1, 9]]) == [5, 8]


if __name__ == "__main__":
    test()
    main()
