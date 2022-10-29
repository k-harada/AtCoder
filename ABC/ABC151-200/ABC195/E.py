def solve(n, s, x):

    xx = x + "."
    possible = [1, 0, 0, 0, 0, 0, 0]

    possible_list = []
    at_list = []

    for i in range(n):
        modulo = int(s[i]) * pow(10, n - 1 - i, 7) % 7
        possible_new = [0, 0, 0, 0, 0, 0, 0]
        for k in range(7):
            if possible[k] == 1:
                possible_new[(k + modulo) % 7] = 1
                possible_new[k] = 1
        possible = possible_new.copy()
        if xx[i] != xx[i + 1]:
            possible_list.append(possible)
            at_list.append(xx[i])
            possible = [1, 0, 0, 0, 0, 0, 0]

    # print(at_list, possible_list)

    k = len(at_list)

    takahashi_win = [1, 0, 0, 0, 0, 0, 0]
    for i in range(k -1, -1, -1):
        takahashi_win_old = takahashi_win.copy()
        possible = possible_list[i]
        if at_list[i] == "A":
            takahashi_win = [1] * 7
            for p in range(7):
                for q in range(7):
                    if possible[q] == 0:
                        continue
                    if takahashi_win_old[(p + q) % 7] == 0:
                        takahashi_win[p] = 0
        else:
            takahashi_win = [0] * 7
            for p in range(7):
                for q in range(7):
                    if possible[q] == 0:
                        continue
                    if takahashi_win_old[(p + q) % 7] == 1:
                        takahashi_win[p] = 1
    if takahashi_win[0]:
        return "Takahashi"
    else:
        return "Aoki"


def main():
    n = int(input())
    s = input()
    x = input()
    res = solve(n, s, x)
    print(res)


def test():
    assert solve(2, "35", "AT") == "Takahashi"
    assert solve(5, "12345", "AAAAT") == "Aoki"
    assert solve(5, "67890", "TTTTA") == "Takahashi"
    assert solve(5, "12345", "ATATA") == "Aoki"


if __name__ == "__main__":
    test()
    main()
