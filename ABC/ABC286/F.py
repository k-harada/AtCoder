def partial_solve(p1, p2, r1, r2):
    for q in range(p2):
        x = q * p1 + r1
        if x % p2 == r2:
            return x


def solve(b_list):
    mod_list = []
    c = 0
    p_list = [4, 9, 5, 7, 11, 13, 17, 19, 23]
    for p in p_list:
        r = b_list[c]
        mod_list.append(r - c - 1)
        c += p
    # print(mod_list)
    res = mod_list[0]
    p1 = 4
    for i in range(1, 9):
        res = partial_solve(p1, p_list[i], res, mod_list[i])
        p1 *= p_list[i]
    return res


def get_a_list():
    res = []
    c = 1
    for p in [4, 9, 5, 7, 11, 13, 17, 19, 23]:
        for d in range(1, p + 1):
            res.append(c + (d % p))
        c += p
    return res


def main():
    m = 108
    a_list = get_a_list()
    print(m)
    print(" ".join([str(a) for a in a_list]))
    b_list = list(map(int, input().split()))
    res = solve(b_list)
    print(res)


def create_n(n):
    res_list = []
    a_list = get_a_list()
    for i in range(108):
        x = i
        for _ in range(n):
            x = a_list[x] - 1
        res_list.append(x + 1)
    return res_list


def test():
    print(solve(get_a_list()))
    b_list = create_n(2)
    # print(b_list)
    print(solve(b_list))


if __name__ == "__main__":
    # test()
    main()
