def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def solve(n, ab_list):
    # factorials
    a, b = ab_list[0]
    fact_a = []
    fact_b = []
    for i in range(1, a):
        if i * i > a:
            break
        elif i * i == a:
            fact_a.append(i)
        elif a % i == 0:
            fact_a.append(i)
            fact_a.append(a // i)
    for i in range(1, b):
        if i * i > b:
            break
        elif i * i == b:
            fact_b.append(i)
        elif b % i == 0:
            fact_b.append(i)
            fact_b.append(b // i)

    fact_a = list(sorted(fact_a))
    fact_b = list(sorted(fact_b))

    a_dict = dict()
    b_dict = dict()
    for i, a in enumerate(fact_a):
        a_dict[a] = i
    for i, b in enumerate(fact_b):
        b_dict[b] = i

    ma = len(fact_a)
    mb = len(fact_b)
    dp = [[0] * (ma * mb) for _ in range(n)]
    dp[0][-1] = 1
    for i in range(1, n):
        a_new, b_new = ab_list[i]
        for j in range(ma * mb):
            if dp[i - 1][j]:
                b_ind = j % mb
                a_ind = j // mb
                a = fact_a[a_ind]
                b = fact_b[b_ind]
                a_new_1 = gcd(a, a_new)
                b_new_1 = gcd(b, b_new)
                new_ind_1 = a_dict[a_new_1] * mb + b_dict[b_new_1]
                dp[i][new_ind_1] = 1
                a_new_2 = gcd(a, b_new)
                b_new_2 = gcd(b, a_new)
                new_ind_2 = a_dict[a_new_2] * mb + b_dict[b_new_2]
                dp[i][new_ind_2] = 1

    res = 1
    for j in range(ma * mb):
        if dp[-1][j] == 1:
            b_ind = j % mb
            a_ind = j // mb
            a = fact_a[a_ind]
            b = fact_b[b_ind]
            res = max(res, lcm(a, b))

    return res


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, ab_list)
    print(res)


def test():
    assert solve(2, [(2, 15), (10, 6)]) == 10
    assert solve(5, [
        (148834018, 644854700), (947642099, 255192490), (35137537, 134714230),
        (944287156, 528403260), (68656286, 200621680)
    ]) == 238630


if __name__ == "__main__":
    test()
    main()
