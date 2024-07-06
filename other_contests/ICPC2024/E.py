def solve(n, a_list):
    res_list = ["Yes"]
    state = [[0] * n for _ in range(n)]
    r2 = n
    for i in range(n):
        if a_list[i] == a_list[-1]:
            r2 = i
            break
    r1 = 0
    for i in range(n - 1, 0, -1):
        if a_list[i] == a_list[0]:
            r1 = i
            break
    if r2 > r1:
        return ["No"]

    if a_list[0] == a_list[-1]:
        for i in range(n):
            state[n - 1][i] = a_list[i]
            state[0][n - 1 - i] = a_list[i]
            state[i][0] = a_list[i]
            state[n - 1 - i][n - 1] = a_list[i]
    else:
        for i in range(r1, r2 + 1):
            state[n - 1][i] = a_list[i]
            state[0][n - 1 - i] = a_list[i]
            state[i][0] = a_list[i]
            state[n - 1 - i][n - 1] = a_list[i]
        for i in range(r2):
            state[r1][i] = a_list[i]
            state[0][n - 1 - r1] = a_list[i]
            state[i][r1] = a_list[i]
            state[n - 1 - i][n - 1 - r1] = a_list[i]
    for i in range(n):
        res_list.append(" ".join([str(a) for a in state[i]]))
    # print(res_list)
    return res_list


def main():
    res = []
    while True:
        n = int(input())
        if n == 0:
            break
        a_list = list(map(int, input().split()))
        res = res + solve(n, a_list)
    for r in res:
        print(r)


def test():
    assert solve(4, [1, 2, 3, 1]) == ["Yes", "1 3 2 1", "2 0 0 3", "3 0 0 2", "1 2 3 1"]
    assert solve(4, [1, 2, 2, 1]) == ["Yes", "1 2 2 1", "2 0 0 2", "2 0 0 2", "1 2 2 1"]
    assert solve(4, [1, 2, 2, 1]) == ["Yes", "1 2 2 1", "2 0 0 2", "2 0 0 2", "1 2 2 1"]
    assert solve(2, [1, 2]) == ["No"]


if __name__ == "__main__":
    test()
    main()
