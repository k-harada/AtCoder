from itertools import chain, combinations


def solve(n, t, a_list):
    if n == 1:
        if a_list[0] <= t:
            return a_list[0]
        else:
            return 0

    m = n // 2
    left_list = []
    right_list = []

    s = a_list[:m]
    for sub in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)):
        left_list.append(sum(sub))
    s = a_list[m:]
    for sub in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)):
        right_list.append(sum(sub))
    # print(left_list, right_list)
    left_list = list(sorted(left_list))
    right_list = list(sorted(right_list, reverse=True))
    left_len = len(left_list)
    right_len = len(right_list)
    i = 0
    j = 0
    res = 0
    while True:
        if left_list[i] + right_list[j] <= t:
            res = max(res, left_list[i] + right_list[j])
            i += 1
            if i == left_len:
                break
        else:
            j += 1
            if j == right_len:
                break
    return res


def main():
    n, t = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, t, a_list)
    print(res)


def test():
    assert solve(5, 17, [2, 3, 5, 7, 11]) == 17
    assert solve(6, 100, [1, 2, 7, 5, 8, 10]) == 33
    assert solve(6, 100, [101, 102, 103, 104, 105, 106]) == 0
    assert solve(7, 273599681, [6706927, 91566569, 89131517, 71069699, 75200339, 98298649, 92857057]) == 273555143


if __name__ == "__main__":
    test()
    main()
