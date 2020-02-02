def solve(n, a_list, b_list):
    a_list_s = sorted(a_list)
    b_list_s = sorted(b_list)

    # check 1
    for i in range(n):
        if a_list_s[i] > b_list_s[i]:
            return "No"

    # check 2
    for i in range(n - 1):
        if a_list_s[i + 1] <= b_list_s[i]:
            return "Yes"

    # check 3
    # do it
    # arg sort
    a_list_s_arg = dict()
    b_list_s_org = dict()
    res_list = [0] * n
    for j in range(n):
        a_list_s_arg[a_list_s[j]] = j
    for k in range(n):
        b_list_s_org[b_list[k]] = k
    for i in range(n):
        j = a_list_s_arg[a_list[i]]
        k = b_list_s_org[b_list_s[j]]
        res_list[i] = k

    i = 0
    cnt = 0
    while True:
        i = res_list[i]
        cnt += 1
        if i == 0:
            break
    if cnt == n:
        return "No"
    else:
        return "Yes"


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, a_list, b_list)
    print(res)


def test():
    assert solve(3, [1, 3, 2], [1, 2, 3]) == "Yes"
    assert solve(3, [1, 2, 3], [2, 2, 2]) == "No"
    assert solve(6, [3, 1, 2, 6, 3, 4], [2, 2, 8, 3, 4, 3]) == "Yes"


if __name__ == "__main__":
    test()
    main()
