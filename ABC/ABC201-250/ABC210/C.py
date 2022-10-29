def solve(n, k, c_list):

    c_count = dict()
    for c in c_list:
        c_count[c] = 0

    for i in range(k):
        c_count[c_list[i]] += 1

    r = len(set(c_list[:k]))
    res = r

    for i in range(n - k):
        c_minus = c_list[i]
        c_plus = c_list[i + k]
        c_count[c_minus] -= 1
        if c_count[c_minus] == 0:
            r -= 1
        c_count[c_plus] += 1
        if c_count[c_plus] == 1:
            r += 1
        res = max(res, r)

    return res


def main():
    n, k = map(int, input().split())
    c_list = list(map(int, input().split()))
    res = solve(n, k, c_list)
    print(res)


def test():
    assert solve(7, 3, [1, 2, 1, 2, 3, 3, 1]) == 3
    assert solve(5, 5, [4, 4, 4, 4, 4]) == 1
    assert solve(10, 6, [
        304621362, 506696497, 304621362, 506696497, 834022578, 304621362, 414720753, 304621362, 304621362, 414720753
    ]) == 4


if __name__ == "__main__":
    test()
    main()
