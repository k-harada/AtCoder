def solve(s):
    visited = [0] * 1000001
    visited[s] = 1
    t = s
    for i in range(2, 1000001):
        if t % 2 == 0:
            t = t // 2
        else:
            t = 3 * t + 1
        if visited[t] != 0:
            return i
        else:
            visited[t] = 1
    return -1


def main():
    s = int(input())
    res = solve(s)
    print(res)


def test():
    assert solve(8) == 5
    assert solve(7) == 18
    assert solve(54) == 114


if __name__ == "__main__":
    test()
    main()
