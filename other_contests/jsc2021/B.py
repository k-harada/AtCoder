def solve(n, m, a_list, b_list):
    v_dict = dict()
    for a in a_list:
        v_dict[a] = 1
    for b in b_list:
        if b in v_dict.keys():
            v_dict[b] += 1
        else:
            v_dict[b] = 1
    res_list = []
    for k in sorted(v_dict.keys()):
        if v_dict[k] == 1:
            res_list.append(k)
    return " ".join([str(res) for res in res_list])


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, m, a_list, b_list)
    print(res)


def test():
    assert solve(2, 2, [1, 2], [1, 3]) == "2 3"
    assert solve(4, 4, [1, 2, 3, 4], [1, 2, 3, 4]) == ""


if __name__ == "__main__":
    test()
    main()
