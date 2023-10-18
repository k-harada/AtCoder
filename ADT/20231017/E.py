def solve(h, w, s, t):
    s_ = ["".join([s[i][j] for i in range(h)]) for j in range(w)]
    t_ = ["".join([t[i][j] for i in range(h)]) for j in range(w)]
    s_2 = "".join(list(sorted(s_)))
    t_2 = "".join(list(sorted(t_)))
    if s_2 == t_2:
        return "Yes"
    else:
        return "No"


def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    res = solve(h, w, s, t)
    print(res)


if __name__ == "__main__":
    main()
