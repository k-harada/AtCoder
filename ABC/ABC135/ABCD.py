LARGE = 10 ** 9 + 7


def solve_a(test=False, a=2, b=16):

    if not test:
        a, b = map(int, input().split())
    if (b - a) % 2 == 0:
        print((a + b) // 2)
    else:
        print("IMPOSSIBLE")


def solve_b(test=False, n=5, p_list=[5, 2, 3, 4, 1]):

    if not test:
        n = int(input())
        p_list = list(map(int, input().split()))

    r = 0
    for i in range(n):
        if p_list[i] != i + 1:
            r += 1
    if r == 0 or r == 2:
        print("YES")
    else:
        print("NO")


def solve_c(test=False, n=2, a_list=[3, 5, 2], b_list=[4, 5]):

    if not test:
        n = int(input())
        a_list = list(map(int, input().split()))
        b_list = list(map(int, input().split()))

    res = 0
    for i in range(n):
        if b_list[i] <= a_list[i]:
            res += b_list[i]
            a_list[i] -= b_list[i]
        elif b_list[i] < a_list[i] + a_list[i + 1]:
            res += b_list[i]
            a_list[i + 1] -= b_list[i] - a_list[i]
            a_list[i] = 0
        else:
            res += a_list[i] + a_list[i + 1]
            a_list[i] = 0
            a_list[i + 1] = 0

    print(res)


def solve_d(test=False, s='??2??5'):

    if not test:
        s = input()

    l = len(s)
    res_list_new = [0] * 13
    res_list_old = [0] * 13
    zero_mod = int(s.replace('?', '0')) % 13
    res_list_new[zero_mod] += 1

    for i in range(1, l + 1):
        if s[-i] == '?':
            for k in range(13):
                res_list_old[k] = res_list_new[k] % LARGE
            base_mod = pow(10, i-1, 13)
            for j in range(1, 10):
                for k in range(13):
                    res_list_new[(k + base_mod * j) % 13] += res_list_old[k]

    print(res_list_new[5] % LARGE)


# solve_a(test=True, a=2, b=16)
# solve_a(test=True, a=0, b=3)
# solve_a(test=True, a=998244353, b=99824435)

# solve_b(test=True, n=5, p_list=[5, 2, 3, 4, 1])
# solve_b(test=True, n=5, p_list=[2, 4, 3, 5, 1])
# solve_b(test=True, n=7, p_list=[1, 2, 3, 4, 5, 6, 7])

# solve_c(test=True, n=2, a_list=[3, 5, 2], b_list=[4, 5])
# solve_c(test=True, n=3, a_list=[5, 6, 3, 8], b_list=[5, 100, 8])
# solve_c(test=True, n=2, a_list=[100, 1, 1], b_list=[1, 100])

# solve_d(test=True, s='??2??5')
# solve_d(test=True, s='?44')
# solve_d(test=True, s='7?4')
# solve_d(test=True, s='?6?42???8??2??06243????9??3???7258??5??7???????774????4?1??17???9?5?70???76???')
