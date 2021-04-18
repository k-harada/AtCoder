def solve(n, s):
    fact_list = [1] * n
    fact_list_3 = [0] * n
    for i in range(1, n):
        c3 = 0
        q = i
        while q % 3 == 0:
            q //= 3
            c3 += 1
        fact_list[i] = (fact_list[i - 1] * q) % 3
        fact_list_3[i] = fact_list_3[i - 1] + c3
    # print(fact_list, fact_list_3)

    res_int = 0
    for i in range(n):
        if i == 0 or i == n - 1:
            ncr_3 = 1
        else:
            c3 = fact_list_3[n - 1] - fact_list_3[i] - fact_list_3[n - 1 - i]
            if c3 > 0:
                ncr_3 = 0
            else:
                ncr_3 = (fact_list[n - 1] * fact_list[i] * fact_list[n - 1 - i]) % 3
        if s[i] == "R":
            res_int += ncr_3
        elif s[i] == "B":
            res_int += 2 * ncr_3
    res_int *= pow(2, n - 1, 3)
    res_int %= 3
    res = "WRB"[res_int]
    return res


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(3, "BWR") == "W"
    assert solve(4, "RRBB") == "W"
    assert solve(6, "BWWRBW") == "B"


if __name__ == "__main__":
    test()
    main()
