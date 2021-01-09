def solve(n, a_list, b_list, p_list):
    for i in range(n):
        if a_list[i] <= b_list[p_list[i] - 1] and p_list[i] != i + 1:
            return ["-1"]
    res = 0
    res_list = []
    a_list_s = sorted([(i, a_list[i]) for i in range(n)], key = lambda x: x[1])
    # print(a_list_s)

    # greedy from light person
    p_list_1 = [p - 1 for p in p_list]
    p_list_inv = [0] * n
    for i in range(n):
        p_list_inv[p_list_1[i]] = i
    # print(p_list_1)
    for i, _ in a_list_s:
        j = p_list_inv[i]
        k = p_list_1[i]
        if i != j:
            res += 1
            p_list_1[i], p_list_1[j] = p_list_1[j], p_list_1[i]
            p_list_inv[i], p_list_inv[k] = p_list_inv[k], p_list_inv[i]
            res_list.append(str(i + 1) + " " + str(j + 1))
        # print(p_list_1)
    # print([str(res)] + res_list)
    return [str(res)] + res_list


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    p_list = list(map(int, input().split()))
    res_list = solve(n, a_list, b_list, p_list)
    for res in res_list:
        print(res)


def test():
    assert solve(4, [3, 4, 8, 6], [5, 3, 1, 3], [3, 4, 2, 1]) == ['3', '1 4', '2 3', '4 3']
    assert solve(4, [1, 2, 3, 4], [4, 3, 2, 1], [4, 3, 2, 1]) == ["-1"]
    assert solve(1, [58], [998244353], [1]) == ["0"]


if __name__ == "__main__":
    test()
    main()
