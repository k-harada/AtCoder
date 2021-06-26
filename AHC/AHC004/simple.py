def solve(n, m, s_list):
    res_list = []
    j = 0
    for i in range(n):
        res = ""
        while j < m:
            if len(res) + len(s_list[j]) <= n:
                res = res + s_list[j]
                j += 1
            else:
                break
        res = res + "." * (n - len(res))
        res_list.append(res)
    return res_list


def main():
    n, m = map(int, input().split())
    s_list = [input() for _ in range(m)]
    res_list = solve(n, m, s_list)
    for res in res_list:
        print(res)


def test():
    print(solve(20, 5, ["A", "ABC", "ABDCKUHMMDSSAHHGJJF", "ABD", "ERABDCKUHMMDSSAHHGJ"]))


if __name__ == "__main__":
    # test()
    main()
