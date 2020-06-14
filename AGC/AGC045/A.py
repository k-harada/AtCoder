def solve(n, a_list, s):

    for i in range(n - 1, -1, -1):
        if s[i] == "0":
            if a_list[i] == 0:
                continue
            r = 2 ** (a_list[i].bit_length() - 1)
            for j in range(i):
                if a_list[j] & r > 0:
                    a_list[j] = a_list[i] ^ a_list[j]
        else:
            if a_list[i] > 0:
                return 1
    return 0


def main():
    t = int(input())
    res_list = []
    for _ in range(t):
        n = int(input())
        a_list = list(map(int, input().split()))
        s = input()
        res = solve(n, a_list, s)
        res_list.append(res)
    for res in res_list:
        print(res)


def test():
    assert solve(2, [1, 2], "10") == 1
    assert solve(2, [1, 1], "10") == 0
    assert solve(6, [2, 3, 4, 5, 6, 7], "111000") == 0


if __name__ == "__main__":
    test()
    main()
