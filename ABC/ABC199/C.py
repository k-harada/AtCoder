def solve(n, s, q, tab_list):
    s_list = list(s)
    flip = 0
    for t, a, b in tab_list:
        if t == 2:
            flip = 1 - flip
        else:
            if flip == 0:
                s_list[a - 1], s_list[b - 1] = s_list[b - 1], s_list[a - 1]
            else:
                if a > n:
                    a = a - n
                else:
                    a = a + n
                if b > n:
                    b = b - n
                else:
                    b = b + n
                s_list[a - 1], s_list[b - 1] = s_list[b - 1], s_list[a - 1]
    if flip == 0:
        return "".join(s_list)
    else:
        return "".join(s_list[n:] + s_list[:n])


def main():
    n = int(input())
    s = input()
    q = int(input())
    tab_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, s, q, tab_list)
    print(res)


def test():
    assert solve(2, "FLIP", 2, [(2, 0, 0), (1, 1, 4)]) == "LPFI"
    assert solve(2, "FLIP", 6, [(1, 1, 3), (2, 0, 0), (1, 1, 2), (1, 2, 3), (2, 0, 0), (1, 1, 4)]) == "ILPF"


if __name__ == "__main__":
    test()
    main()
