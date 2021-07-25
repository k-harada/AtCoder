def solve(n, a_list, b_list):

    v_dict = dict()
    for b in b_list:
        v_dict[b] = 0

    res = []
    # try
    for i in range(n):
        # initialize
        for b in b_list:
            v_dict[b] = 0
        for b in b_list:
            v_dict[b] += 1

        x = a_list[0] ^ b_list[i]
        success = True
        for j in range(1, n):
            b = a_list[j] ^ x
            if b in v_dict.keys():
                if v_dict[b] == 0:
                    success = False
                else:
                    v_dict[b] -= 1
            else:
                success = False
        if success:
            res.append(x)

    return [len(set(res))] + list(sorted(list(set(res))))


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, a_list, b_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [1, 2, 3], [6, 4, 7]) == [1, 5]
    assert solve(2, [0, 1], [0, 2]) == [0]
    # print(solve(2000, list(range(2000)), list(range(2000))))


if __name__ == "__main__":
    test()
    main()
