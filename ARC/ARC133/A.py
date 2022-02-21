def solve(n, a_list):
    x = a_list[0]
    for i in range(n):
        if x > a_list[i]:
            break
        elif x == a_list[i]:
            pass
        else:
            x = a_list[i]
    res_list = []
    for a in a_list:
        if a != x:
            res_list.append(str(a))
    return " ".join(res_list)


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(5, [2, 4, 4, 1, 2]) == "2 1 2"
    assert solve(3, [1, 1, 1]) == ""
    assert solve(5, [1, 1, 2, 3, 3]) == "1 1 2"


if __name__ == "__main__":
    test()
    main()
