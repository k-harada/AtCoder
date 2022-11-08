def solve(n, h_list):

    res = 0
    d_list = [d for d in h_list]
    d_list.append(0)
    while max(d_list) > 0:
        s = -1
        for i in range(n + 1):
            if d_list[i] > 0 and s == -1:
                s = i
            if d_list[i] == 0 and s != -1:
                # print(s, i)
                m = min(d_list[s:i])
                res += m
                for j in range(s, i):
                    d_list[j] -= m
                s = -1
        # print(d_list)

    return res


def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    res = solve(n, h_list)
    print(res)


def test():
    assert solve(4, [1, 2, 2, 1]) == 2
    assert solve(5, [3, 1, 2, 3, 1]) == 5
    assert solve(8, [4, 23, 75, 0, 23, 96, 50, 100]) == 221


if __name__ == "__main__":
    test()
    main()
