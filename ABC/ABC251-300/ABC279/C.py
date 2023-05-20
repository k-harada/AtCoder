def solve(h, w, s, t):
    s_ = list(sorted(["".join([s[i][j] for i in range(h)]) for j in range(w)]))
    t_ = list(sorted(["".join([t[i][j] for i in range(h)]) for j in range(w)]))
    for j in range(w):
        if s_[j] != t_[j]:
            return "No"
    return "Yes"


def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    t = [list(input()) for _ in range(h)]
    res = solve(h, w, s, t)
    print(res)


if __name__ == "__main__":
    main()
