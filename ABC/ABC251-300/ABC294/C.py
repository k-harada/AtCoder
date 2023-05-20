def solve(n, m, a_list, b_list):
    i = 0
    j = 0
    k = 1
    res_a = []
    res_b = []
    while True:
        if i == n and j == m:
            break
        elif i == n:
            res_b.append(k)
            j += 1
        elif j == m:
            res_a.append(k)
            i += 1
        elif a_list[i] < b_list[j]:
            res_a.append(k)
            i += 1
        else:
            res_b.append(k)
            j += 1
        k += 1
    return [" ".join([str(a) for a in res_a]), " ".join([str(b) for b in res_b])]


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, m, a_list, b_list)
    for r in res:
        print(r)


def test():
    assert solve(4, 3, [3, 14, 15, 92], [6, 53, 58]) == ["1 3 4 7", "2 5 6"]
    assert solve(4, 4, [1, 2, 3, 4], [100, 200, 300, 400]) == ["1 2 3 4", "5 6 7 8"]
    assert solve(8, 12, [3, 4, 10, 15, 17, 18, 22, 30], [5, 7, 11, 13, 14, 16, 19, 21, 23, 24, 27, 28]) == [
        "1 2 5 9 11 12 15 20", "3 4 6 7 8 10 13 14 16 17 18 19"
    ]


if __name__ == "__main__":
    test()
    main()
