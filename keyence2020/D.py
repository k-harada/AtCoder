from itertools import product


def solve(n, a_list, b_list):

    res = 10 ** 9 + 7

    for p in product([0, 1], repeat=n):
        if sum(p) % 2 == 1:
            continue

        r = 0

        c_list = [a for a in a_list]
        for i in range(n):
            if p[i] == 1:
                c_list[i] = b_list[i]
        c_list_s = list(sorted(c_list))

        used = [0] * n
        d_list = [0] * n
        for k in range(n):
            j = -1
            for i in range(n):
                if c_list[i] == c_list_s[k] and not used[i] and (i - k + p[i]) % 2 == 0:
                    used[i] = 1
                    j = i
                    break
            if j >= 0:
                d_list[j] = k
            else:
                r += 10 ** 9 + 7

        # r
        for i in range(n - 1):
            for j in range(i + 1, n):
                if d_list[i] > d_list[j]:
                    r += 1

        res = min(res, r)
    # print(res)
    if res < 10 ** 9 + 7:
        return res
    else:
        return -1


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, a_list, b_list)
    print(res)


def test():
    assert solve(3, [3, 4, 3], [3, 2, 3]) == 1
    assert solve(2, [2, 1], [1, 2]) == -1
    assert solve(4, [1, 2, 3, 4], [5, 6, 7, 8]) == 0


if __name__ == "__main__":
    test()
    main()
