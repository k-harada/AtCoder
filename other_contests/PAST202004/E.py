def solve(n, a_list):
    res_list = []
    for i in range(n):
        res = 0
        x = i
        while True:
            x = a_list[x] - 1
            res += 1
            if x == i:
                break
        res_list.append(str(res))

    return " ".join(res_list)


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(6, [1, 3, 2, 5, 6, 4]) == "1 2 2 3 3 3"
    assert solve(3, [3, 2, 1]) == "2 1 2"
    assert solve(2, [1, 2]) == "1 1"


if __name__ == "__main__":
    test()
    main()
