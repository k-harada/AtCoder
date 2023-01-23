def solve_sub(n, a_list, b_list):
    a_min = min(a_list)
    av_list = [a_min]
    for j in range(n):
        if a_list[j] == a_min:
            j0 = j
            break
    for j in range(j0, n):
        if a_list[j] != av_list[-1]:
            av_list.append(a_list[j])
    for j in range(j0):
        if a_list[j] != av_list[-1]:
            av_list.append(a_list[j])

    b_min = min(b_list)
    bv_list = [b_min]
    for j in range(n):
        if b_list[j] == b_min:
            j0 = j
            break
    for j in range(j0, n):
        if b_list[j] != bv_list[-1]:
            bv_list.append(b_list[j])
    for j in range(j0):
        if b_list[j] != bv_list[-1]:
            bv_list.append(b_list[j])

    # print(av_list, bv_list)
    if len(av_list) >= 3 and av_list[-1] == av_list[0]:
        _ = av_list.pop()
    if len(bv_list) >= 3 and bv_list[-1] == bv_list[0]:
        _ = bv_list.pop()
    # 例外ケース
    if len(bv_list) == n:
        if a_list == b_list:
            return "Yes"
        else:
            return "No"

    dp = [[-1] * (len(bv_list)) for _ in range(2 * len(av_list))]
    for j in range(2 * len(av_list)):
        a = av_list[j % len(av_list)]
        if j > 0:
            for i in range(len(bv_list)):
                dp[j][i] = dp[j - 1][i]
        for k, v in enumerate(bv_list):
            if v == a:
                if k == 0:
                    dp[j][k] = j
                elif j > 0:
                    dp[j][k] = dp[j - 1][k - 1]
    # print(dp)
    for j in range(2 * len(av_list)):
        if dp[j][-1] > 0 and j - dp[j][-1] < len(av_list):
            return "Yes"
    return "No"


def solve(t, case_list):
    res = []
    for i in range(t):
        n, a_list, b_list = case_list[i]
        res.append(solve_sub(n, a_list, b_list))

    return res


def main():
    t = int(input())
    case_list = []
    for _ in range(t):
        n = int(input())
        a_list = list(map(int, input().split()))
        b_list = list(map(int, input().split()))
        case_list.append((n, a_list, b_list))
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [(2, [1, 2], [2, 2]), (4, [2, 3, 1, 1], [2, 1, 1, 2]), (2, [1, 1], [2, 2])]) == ["Yes", "Yes", "No"]


if __name__ == "__main__":
    test()
    main()
