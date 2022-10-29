from bisect import bisect_right


def solve(n, q, a_list, k_list):
    v_list = [0]
    b_list = [0]
    for i in range(n):
        v_list.append(a_list[i] - i)
        b_list.append(a_list[i] + 1)
    # print(v_list)
    # print(b_list)
    res_list = []
    for k in k_list:
        v = bisect_right(v_list, k) - 1
        res = b_list[v] + k - v_list[v]
        res_list.append(res)
    # print(res_list)
    return res_list


def main():
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    k_list = [int(input()) for _ in range(q)]
    res_list = solve(n, q, a_list, k_list)
    for res in res_list:
        print(res)


def test():
    assert solve(4, 3, [3, 5, 6, 7], [2, 5, 3]) == [2, 9, 4]
    assert solve(5, 2, [1, 2, 3, 4, 5], [1, 10]) == [6, 15]


if __name__ == "__main__":
    test()
    main()