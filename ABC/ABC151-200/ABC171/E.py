def solve(n, a_list):
    s = 0
    for i in range(n):
        a = a_list[i]
        s = s ^ a
    res_list = []
    for i in range(n):
        a = a_list[i]
        res_list.append(str(s ^ a))
    # print(res_list)
    return " ".join(res_list)


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(4, [20, 11, 9, 24]) == "26 5 7 22"


if __name__ == "__main__":
    test()
    main()
