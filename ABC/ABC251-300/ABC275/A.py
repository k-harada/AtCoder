def solve(n, h_list):
    res = 0
    highest = 0
    for i in range(n):
        h = h_list[i]
        if h > highest:
            highest = h
            res = i + 1
    return res


def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    res = solve(n, h_list)
    print(res)


def test():
    assert solve(3, [50, 80, 70]) == 2
    assert solve(1, [1000000000]) == 1
    assert solve(10, [22, 75, 26, 45, 72, 81, 47, 29, 97, 2]) == 9


if __name__ == "__main__":
    test()
    main()
