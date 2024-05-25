def solve(n, a_list):
    filled = [0] * (n + 1)
    path = []
    p = 1
    while True:
        if filled[p] == 1:
            break
        path.append(p)
        filled[p] = 1
        p = a_list[p - 1]
    for i in range(len(path)):
        if path[i] == p:
            path = path[i:]
            break
    return [len(path), " ".join([str(p) for p in path])]


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    for r in res:
        print(r)


def test():
    assert solve(7, [6, 7, 2, 1, 3, 4, 5]) == [3, "1 6 4"]
    assert solve(2, [2, 1]) == [2, "1 2"]
    assert solve(8, [3, 7, 4, 7, 3, 3, 8, 2]) == [3, "7 8 2"]


if __name__ == "__main__":
    test()
    main()
