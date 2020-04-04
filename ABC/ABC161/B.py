def solve(n, m, a_list):
    cnt = 0
    if sum(a_list) % (4 * m) == 0:
        bar = sum(a_list) // (4 * m)
    else:
        bar = sum(a_list) // (4 * m) + 1
    for a in a_list:
        if a >= bar:
            cnt += 1
    if cnt >= m:
        return "Yes"
    else:
        return "No"


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(4, 1, [5, 4, 2, 1]) == "Yes"
    assert solve(3, 2, [300, 19, 1]) == "No"
    assert solve(12, 3, [4, 56, 78, 901, 2, 345, 67, 890, 123, 45, 6, 789]) == "Yes"


if __name__ == "__main__":
    test()
    main()
