test = False


def solve_a(test=False, a=0, b=0, c=0):
    if not test:
        a, b, c = map(int, input().split())
    d = max(c - (a - b), 0)
    print(d)


def solve_b(test=False, n=0):
    if not test:
        n = int(input())
    res = 0
    for i in range(1, n + 1):
        if len(str(i)) % 2 == 1:
            res += 1
    print(res)


def solve_c(test=False, n=0, h_list=[]):
    if not test:
        n = int(input())
        h_list = list(map(int, input().split()))
    res = 'Yes'
    new_h_list = [0] * n
    new_h_list[0] = h_list[0] - 1

    for i in range(1, n):
        # cannot down
        if h_list[i] == new_h_list[i - 1]:
            new_h_list[i] = h_list[i]
        elif h_list[i] < new_h_list[i - 1]:
            new_h_list[i] = h_list[i]
            res = 'No'
        else:
            new_h_list[i] = h_list[i] - 1
    print(res)


if __name__ == "__main__":
    if test:
        solve_a(test=True, a=6, b=4, c=3)
        solve_a(test=True, a=8, b=3, c=9)
        solve_a(test=True, a=12, b=3, c=7)
        solve_b(test=True, n=11)
        solve_b(test=True, n=136)
        solve_b(test=True, n=100000)
        solve_c(test=True, n=5, h_list=[1, 2, 1, 1, 3])
        solve_c(test=True, n=4, h_list=[1, 3, 2, 1])
        solve_c(test=True, n=5, h_list=[1, 2, 3, 4, 5])
        solve_c(test=True, n=1, h_list=[1000000000])
    else:
        solve_a()
        # solve_b()
        # solve_c()
