def solve(n, s_list):
    res_list = ["X"] * n
    for i in range(n // 2):
        for c in s_list[i]:
            if c in s_list[n - 1 - i]:
                res_list[i] = c
                res_list[n - 1 - i] = c
                break
    if n % 2 == 1:
        res_list[n // 2] = s_list[n // 2][0]

    if "X" in res_list:
        return "-1"
    return "".join(res_list)


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    print(res)


def test():
    assert solve(2, ["yc", "ys"]) == "yy"
    assert solve(2, ["rv", "jh"]) == "-1"


if __name__ == "__main__":
    test()
    main()
