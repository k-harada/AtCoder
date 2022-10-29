submit = True


def solve_e(test=False, n=2, k=3, a_list=[8, 20]):

    if not test:
        n, k = map(int, input().split())
        a_list = list(map(int, input().split()))

    a_sum = sum(a_list)
    q_list = []

    for i in range(1, int(a_sum ** 0.5)+1):
        if a_sum % i == 0:
            q_list.append(i)
            if i != a_sum // i:
                q_list.append(a_sum // i)

    res = 1
    for q in q_list:
        r_list = [0] * n
        for i in range(n):
            r_list[i] = a_list[i] % q
        r_list_s = sorted(r_list)
        cnt = 0
        right = n - 1
        for i in range(n):
            if r_list_s[i] == q:
                break
            r = r_list_s[i]
            cnt += r
            while r > 0:
                d = q - r_list_s[right]
                if r >= d:
                    r -= d
                    r_list_s[right] = q
                    right -= 1
                else:
                    r_list_s[right] += r
                    r = 0
            r_list_s[i] = 0
        if cnt <= k:
            if q > res:
                res = q

    print(res)


if __name__ == "__main__":
    if submit:
        solve_e()
    else:
        solve_e(test=True, n=2, k=3, a_list=[8, 20])
        solve_e(test=True, n=2, k=10, a_list=[3, 5])
        solve_e(test=True, n=4, k=5, a_list=[10, 1, 2, 22])
        solve_e(test=True, n=8, k=7, a_list=[1, 7, 5, 6, 8, 2, 6, 5])

