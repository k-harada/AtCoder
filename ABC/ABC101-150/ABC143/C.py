def solve_c(n, s):
    res = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            res += 1
    return res


def main():
    n = int(input())
    s = input()
    res = solve_c(n, s)
    print(res)


def test():
    assert solve_c(10, "aabbbbaaca") == 5
    assert solve_c(5, "aaaaa") == 1
    assert solve_c(20, "xxzaffeeeeddfkkkkllq") == 10


if __name__ == "__main__":
    test()
    main()
