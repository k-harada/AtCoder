from bisect import bisect_left


def solve_d(n, a_list, b_list):
    a_list_sub = [a_list[i] for i in range(n) if a_list[i] < b_list[i]]
    b_list_sub = [b_list[i] for i in range(n) if a_list[i] < b_list[i]]
    a_list_add = [(a_list[i], i) for i in range(n) if a_list[i] >= b_list[i]]

    le = len(a_list_sub)
    if le == 0:
        return 0, 1
    a_sum = sum(a_list_sub)
    b_list_sub_s = sorted(b_list_sub, reverse=True)
    b_list_sub_cum = [0]
    for i, b in enumerate(b_list_sub_s):
        b_list_sub_cum.append(b_list_sub_cum[i] + b)

    r = bisect_left(b_list_sub_cum, a_sum) - 1
    q_max = b_list_sub_s[r]
    p_max = q_max * (le - r) - (a_sum - b_list_sub_cum[r])
    q_max *= n
    # print(le, p_max, q_max, r, a_sum - b_list_sub_cum[r])
    a_list_add_s = sorted(a_list_add, key=lambda x:x[0])
    for a, i in a_list_add_s:
        le += 1
        a_sum += a
        b_list_sub_cum.append(b_list_sub_cum[-1] + b_list[i])
        b_list_sub_s.append(b_list[i])

        r = bisect_left(b_list_sub_cum, a_sum) - 1
        if r >= len(b_list_sub_s):
            q = 1
            p = 0
        else:
            q = b_list_sub_s[r]
            p = q * (le - r) - (a_sum - b_list_sub_cum[r])
            q *= n
        # print(le, p, q)

        if p * q_max > p_max * q:
            p_max, q_max = p, q
    return p_max, q_max


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def main():
    n = int(input())
    a_list = [0] * n
    b_list = [0] * n
    for i in range(n):
        a, b = map(int, input().split())
        a_list[i] = a
        b_list[i] = b
    p, q = solve_d(n, a_list, b_list)
    r = gcd(p, q)
    print(p // r, q // r)


if __name__ == "__main__":
    main()
