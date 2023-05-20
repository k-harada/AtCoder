def solve(n, a_list):
    a_dict = dict()
    for a in a_list:
        if a not in a_dict.keys():
            a_dict[a] = 1
        else:
            a_dict[a] += 1
    kv_list = []
    for k in a_dict.keys():
        v = a_dict[k]
        kv_list.append((k, v))
    kv_list = list(sorted(kv_list, key=lambda x: x[0], reverse=True))
    # print(kv_list)
    res = [0] * n
    m = len(kv_list)
    for i in range(m):
        res[i] = kv_list[i][1]
    # print(res)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    for r in res:
        print(r)


def test():
    assert solve(6, [2, 7, 1, 8, 2, 8]) == [2, 1, 2, 1, 0, 0]
    assert solve(1, [1]) == [1]
    assert solve(10, [
        979861204, 57882493, 979861204, 447672230, 644706927, 710511029, 763027379, 710511029, 447672230, 136397527
    ]) == [2, 1, 2, 1, 2, 1, 1, 0, 0, 0]


if __name__ == "__main__":
    test()
    main()
