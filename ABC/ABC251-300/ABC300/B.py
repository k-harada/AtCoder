def solve(h, w, a, b):
    for s in range(h):
        for t in range(w):
            flag = 1
            for i in range(h):
                for j in range(w):
                    if a[(i + s) % h][(j + t) % w] != b[i][j]:
                        flag = 0
            if flag == 1:
                return "Yes"
    return "No"


def main():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    b = [list(input()) for _ in range(h)]
    res = solve(h, w, a, b)
    print(res)


if __name__ == "__main__":
    main()
