from collections import Counter


def solve(n, a_list, b_list):
    count_a = Counter(a_list)
    count_b = Counter(b_list)
    count_ab = dict()
    for k in count_a.keys():
        if k in count_b.keys():
            if count_a[k] + count_b[k] > n:
                return ["No"]
            count_ab[k] = min(count_a[k], count_b[k])

    # move a
    a_list_1 = []
    a_list_2 = []
    a = 0
    for i in range(n):
        if a != a_list[i]:
            if a_list[i] in count_ab.keys():
                c = count_ab[a_list[i]]
            else:
                c = 0
        a = a_list[i]
        if c > 0:
            a_list_1.append(a)
            c -= 1
        else:
            a_list_2.append(a)
    # move b
    b_list_1 = []
    b_list_2 = []
    b = 0
    for i in range(n):
        if b != b_list[i]:
            if b_list[i] in count_ab.keys():
                c = count_ab[b_list[i]]
            else:
                c = 0
        b = b_list[i]
        if c > 0:
            b_list_1.append(b)
            c -= 1
        else:
            b_list_2.append(b)
    # print(a_list_1, a_list_2, b_list_1, b_list_2)
    k_max = -1
    if len(count_ab.values()) == 0:
        return ["Yes", " ".join([str(b) for b in b_list])]
    d = max(count_ab.values())
    for k in count_ab.keys():
        if count_ab[k] == d:
            k_max = k
            break
    a_list_moved = a_list_1 + a_list_2
    b_list_moved = b_list_1[d:] + b_list_1[:d] + b_list_2

    # need to modify
    if d * 2 > len(a_list_1):
        # a includes many k_max
        if count_a[k_max] >= count_b[k_max]:
            # swap a
            j = len(a_list_1)
            for i in range(len(a_list_1)):
                if a_list_moved[i] == b_list_moved[i] == k_max:
                    while a_list_moved[j] == k_max:
                        j += 1
                    a_list_moved[i], a_list_moved[j] = a_list_moved[j], a_list_moved[i]
        else:
            # swap b
            j = len(a_list_1)
            for i in range(len(a_list_1)):
                if a_list_moved[i] == b_list_moved[i] == k_max:
                    while b_list_moved[j] == k_max:
                        j += 1
                    b_list_moved[i], b_list_moved[j] = b_list_moved[j], b_list_moved[i]
    # print(a_list_moved, b_list_moved)
    res_ab = list(sorted([(a, b) for a, b in zip(a_list_moved, b_list_moved)], key=lambda x: x[0]))
    res_b = " ".join([str(ab[1]) for ab in res_ab])
    # print(res_b)
    return ["Yes", res_b]


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, a_list, b_list)
    for r in res:
        print(r)


def test():
    assert solve(6, [1, 1, 1, 2, 2, 3], [1, 1, 1, 2, 2, 3]) == ["Yes", "2 2 3 1 1 1"]
    assert solve(3, [1, 1, 2], [1, 1, 3]) == ["No"]
    assert solve(4, [1, 1, 2, 3], [1, 2, 3, 3]) == ["Yes", "2 3 3 1"]


if __name__ == "__main__":
    test()
    main()
