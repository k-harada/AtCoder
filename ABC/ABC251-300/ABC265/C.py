def solve(h, w, g):
    i = 0
    j = 0
    visited = [[0] * w for _ in range(h)]

    while True:
        if visited[i][j]:
            return "-1"
        visited[i][j] = 1
        if g[i][j] == "U":
            if i == 0:
                return f"{i + 1} {j + 1}"
            i -= 1
        elif g[i][j] == "D":
            if i == h - 1:
                return f"{i + 1} {j + 1}"
            i += 1
        elif g[i][j] == "L":
            if j == 0:
                return f"{i + 1} {j + 1}"
            j -= 1
        else:
            if j == w - 1:
                return f"{i + 1} {j + 1}"
            j += 1

    return "WA"


def main():
    h, w = map(int, input().split())
    g = [input() for _ in range(h)]
    res = solve(h, w, g)
    print(res)


def test():
    assert solve(2, 3, ["RDU", "LRU"]) == "1 3"
    assert solve(2, 3, ["RRD", "ULL"]) == "-1"


if __name__ == "__main__":
    test()
    main()
