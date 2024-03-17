def solve(n):
    phi_list = [1] * (n + 1)
    phi_rev = [1] * (n + 1)
    q_list = [1] * (n + 1)
    for i in range(2, n + 1):
        phi = i - phi_rev[i]
        phi_list[i] = phi
        q_list[i] += 1
        for j in range(2 * i, n + 1, i):
            phi_rev[j] += phi
            q_list[j] += 1
    # print(phi_list[:20])
    # print(q_list[:20])
    res = 0
    for i in range(2, n + 1):
        res += i - phi_list[i] - q_list[i] + 1
    # print(res)
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(9) == 3
    assert solve(1) == 0
    assert solve(231125) == 10469378012


if __name__ == "__main__":
    # test()
    main()
