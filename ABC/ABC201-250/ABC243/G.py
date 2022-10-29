import math


def solve(t, x_list):
    ans_list = [0] * (10 ** 6)
    ans_list[1] = 1
    i = 1
    c = 1
    for j in range(2, 10 ** 6):
        if j >= (i + 1) ** 2:
            c += ans_list[i + 1]
            i += 1
        ans_list[j] = c
    s = sum(ans_list)

    res = []
    for x in x_list:
        rt = int(math.sqrt(x))
        if rt ** 2 > x:
            rt -= 1
        elif (rt + 1) ** 2 <= x:
            rt += 1

        if x < 10 ** 6:
            res.append(ans_list[x])
        elif x < 10 ** 12:
            res.append(sum(ans_list[:(rt + 1)]))
        else:
            r = s
            a = 10 ** 6 - 1
            c = sum(ans_list[:1000])
            for d in range(1000, 1000000):
                if a + 2 * d + 1 < rt:
                    a += 2 * d + 1
                    c += ans_list[d]
                    r += c * (2 * d + 1)
                else:
                    c += ans_list[d]
                    r += c * (rt - a)
                    break
            res.append(r)
    # print(res)
    return res


def main():
    t = int(input())
    x_list = [int(input()) for _ in range(t)]
    res = solve(t, x_list)
    for r in res:
        print(r)


def test():
    assert solve(6, [
        16, 17, 1, 123456789012, 1000000000000000000, 1000000000000000000
    ]) == [5, 5, 1, 4555793983, 23561347048791096, 23561347048791096]


if __name__ == "__main__":
    test()
    main()
