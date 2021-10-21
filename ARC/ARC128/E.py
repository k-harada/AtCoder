def solve(n, k, a_list):
    s = sum(a_list)
    res = [0] * s
    count = [a for a in a_list]
    m = 0
    i = 0
    j = 0
    while i < n:
        if count[i] > 0:
            count[i] -= 1
            while res[j] > 0:
                j += 1
            res[j] = i + 1
            j += 1
            m += 1
        i += 1
        if m == k:
            i = 0
    print(res)
    return " ".join([str(r) for r in res])


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(3, 3, [2, 2, 1]) == "1 2 3 1 2"
    assert solve(3, 2, [2, 1, 2]) == "1 2 3 1 3"
    assert solve() == 0


if __name__ == "__main__":
    test()
    main()
