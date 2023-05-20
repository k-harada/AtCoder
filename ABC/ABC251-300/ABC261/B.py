def solve(n, a):
    for i in range(n - 1):
        for j in range(i + 1, n):
            ij = a[i][j]
            ji = a[j][i]
            if ij == ji == "D":
                continue
            elif ij == "W" and ji == "L":
                continue
            elif ij == "L" and ji == "W":
                continue
            else:
                return "incorrect"
    return "correct"


def main():
    n = int(input())
    a = [list(input()) for _ in range(n)]
    res = solve(n, a)
    print(res)


if __name__ == "__main__":
    main()
