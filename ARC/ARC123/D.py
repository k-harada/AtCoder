def solve(n, a_list):
    b_list = [a_list[0]]
    c_list = [0]
    for i in range(1, n):
        if a_list[i] >= a_list[i - 1]:
            b_list.append(b_list[-1] + a_list[i] - a_list[i - 1])
            c_list.append(c_list[-1])
        else:
            b_list.append(b_list[-1])
            c_list.append(c_list[-1] + a_list[i] - a_list[i - 1])

    bc_list = b_list + [-c for c in c_list]
    bc_list_s = list(sorted(bc_list))
    median = bc_list_s[n]
    res = sum([abs(x - median) for x in bc_list_s])
    # print(b_list, c_list)
    # print(res)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [1, -2, 3]) == 10
    assert solve(4, [5, 4, 3, 5]) == 17
    assert solve(1, [-10]) == 10


if __name__ == "__main__":
    test()
    main()
