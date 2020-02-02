def solve(n, a_list):
    cnt_list = [0] * n
    for i in range(n):
        cnt_list[a_list[i] - 1] += 1
    cnt_0 = -1
    cnt_2 = -1
    for i in range(n):
        if cnt_list[i] == 0:
            cnt_0 = i + 1
        elif cnt_list[i] == 2:
            cnt_2 = i + 1
    if cnt_0 == -1:
        return "Correct"
    else:
        return str(cnt_2) + " " + str(cnt_0)


def main():
    n = int(input())
    a_list = [0] * n
    for i in range(n):
        a = int(input())
        a_list[i] = a
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(6, [1, 5, 6, 3, 2, 6]) == "6 4"
    assert solve(7, [5, 4, 3, 2, 7, 6, 1]) == "Correct"


if __name__ == "__main__":
    test()
    main()
