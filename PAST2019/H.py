def solve(n, c_list, q, s_list):

    res = 0

    dec_list_n = [0] * n
    global_dec = 0
    odd_dec = 0
    global_min = min(c_list)
    odd_min = min(c_list[0::2])

    for i in range(q):
        s = s_list[i]
        if s[0] == "1":
            _, x, a = map(int, s.split())
            x -= 1
            if x % 2 == 0:
                x_res = c_list[x] - global_dec - odd_dec - dec_list_n[x]
                if x_res >= a:
                    dec_list_n[x] += a
                    res += a
                    odd_min = min(odd_min, x_res - a)
                    global_min = min(global_min, x_res - a)
            else:
                x_res = c_list[x] - global_dec - dec_list_n[x]
                if x_res >= a:
                    dec_list_n[x] += a
                    res += a
                    global_min = min(global_min, x_res - a)
        elif s[0] == "2":
            _, a = map(int, s.split())
            if odd_min >= a:
                odd_dec += a
                odd_min -= a
                res += a * ((n + 1) // 2)
                global_min = min(global_min, odd_min)
        else:
            _, a = map(int, s.split())
            if global_min >= a:
                global_dec += a
                global_min -= a
                odd_min -= a
                res += a * n

    return res


def main():
    n = int(input())
    c_list = list(map(int, input().split()))
    q = int(input())
    s_list = [""] * q
    for i in range(q):
        s = input()
        s_list[i] = s
    res = solve(n, c_list, q, s_list)
    print(res)


def test():
    assert solve(4, [5, 3, 3, 5], 6, ["1 2 1", "2 2", "2 2", "3 100", "3 1", "1 1 3"]) == 9
    assert solve(2, [3, 4], 3, ["1 2 9", "2 4", "3 4"]) == 0


if __name__ == "__main__":
    test()
    main()
