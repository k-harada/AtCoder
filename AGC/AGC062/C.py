def solve(n, k, a_list):
    a_list_s = list(sorted(a_list))
    if a_list_s[0] > k:
        return " ".join([str(i + 1) for i in range(k)])
    s = a_list_s[0]
    sets = [dict() for _ in range(n + 1)]
    for x in range(1, a_list_s[0]):
        sets[1][x] = 1
    for i_, a in enumerate(a_list_s[1:]):
        i = i_ + 1
        if s < a:
            if len(sets[i]) + (a - s - 1) >= k:
                res_fin = list(sorted(list(sets[i].keys()) + list(range(s + 1, s + 1 + k))))[:k]
                # print(res_fin)
                return " ".join([str(a) for a in res_fin])
            else:
                for x in sets[i].keys():
                    sets[i + 1][x] = 1
                for x in range(s + 1, a):
                    sets[i + 1][x] = 1
                for x in sets[i].keys():
                    sets[i + 1][x + a] = 1
        else:
            for x in sets[i].keys():
                if x < a:
                    sets[i + 1][x] = 1
            if len(sets[i + 1]) >= k:
                res_fin = list(sorted(list(sets[i + 1].keys())))[:k]
                # print(res_fin)
                return " ".join([str(a) for a in res_fin])
            for x in sets[i].keys():
                if x <= a:
                    pass
                else:
                    if x - a in sets[i].keys():
                        sets[i + 1][x] = 1
            for x in sets[i].keys():
                if x + a > s:
                    sets[i + 1][x + a] = 1
        s += a
        # print(sets)
    res_fin = list(sorted(list(sets[n].keys())))
    if len(res_fin) < k:
        for d in range(k - len(res_fin)):
            res_fin.append(s + d + 1)
    return " ".join([str(a) for a in res_fin[:k]])


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(3, 3, [1, 2, 5]) == "4 9 10"
    assert solve(20, 10, [
        324, 60, 1, 15, 60, 15, 1, 60, 319, 1, 327, 1, 2, 60, 2, 345, 1, 2, 2, 15
    ]) == "14 29 44 59 74 89 104 119 134 149"
    assert solve(10, 10, [
        1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024
    ]) == "2048 2049 2050 2051 2052 2053 2054 2055 2056 2057"


if __name__ == "__main__":
    test()
    main()
