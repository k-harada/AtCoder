def solve(n, k, a_list):

    m = max(a_list)
    small_list = []
    j = 0
    for i in range(1, m):
        if i == a_list[j]:
            j += 1
        else:
            small_list.append(i)
    len_sm = len(small_list)
    # print(small_list)
    # print(large_list)
    res_list = []
    j = 0
    for i in range(k):
        # add small number
        if i > 0 and j < len_sm:
            if small_list[j] < a_list[i - 1]:
                res_list.append(small_list[j])
                j += 1
        # if last, insert large ones
        if i == k - 1:
            for v in range(n, m, -1):
                res_list.append(v)
        # add a
        res_list.append(a_list[i])
    # add small ones
    todo = n - len(res_list)
    for i in range(todo):
        res_list.append(small_list[-(i + 1)])
    # print(res_list)
    return " ".join([str(r) for r in res_list])


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(3, 2, [2, 3]) == "2 1 3"
    assert solve(5, 1, [4]) == "5 4 3 2 1"


if __name__ == "__main__":
    test()
    main()
