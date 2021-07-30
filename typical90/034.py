def solve(n, k, a_list):
    v_dict = dict()
    for a in a_list:
        v_dict[a] = 0

    v_unique = 0
    i = 0
    j = 0
    res = 0

    while j < n:
        a_i = a_list[i]
        a_j = a_list[j]
        if v_unique < k or (v_unique == k and v_dict[a_j] > 0):
            if v_dict[a_j] == 0:
                v_unique += 1
            v_dict[a_j] += 1
            j += 1
        else:
            v_dict[a_i] -= 1
            if v_dict[a_i] == 0:
                v_unique -= 1
            i += 1
        res = max(res, j - i)

    return res


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(5, 1, [1, 2, 3, 4, 5]) == 1
    assert solve(5, 4, [1, 1, 2, 4, 2]) == 5
    assert solve(10, 2, [1, 2, 3, 4, 4, 3, 2, 1, 2, 3]) == 4


if __name__ == "__main__":
    test()
    main()
