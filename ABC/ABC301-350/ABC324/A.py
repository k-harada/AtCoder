def solve(n, a_list):
    if min(a_list) == max(a_list):
        return "Yes"
    else:
        return "No"


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [3, 2, 4]) == "No"
    assert solve(4, [3, 3, 3, 3]) == "Yes"
    assert solve(10, [73, 8, 55, 26, 97, 48, 37, 47, 35, 55]) == "No"


if __name__ == "__main__":
    test()
    main()
