def solve(n, m, s_list):
    odd = 0
    even = 0
    for s in s_list:
        if s.count("1") % 2 == 0:
            even += 1
        else:
            odd += 1
    return even * odd


def main():
    n, m = map(int, input().split())
    s_list = [input() for _ in range(n)]
    res = solve(n, m, s_list)
    print(res)


def test():
    assert solve(3, 2, ["00", "01", "10"]) == 2
    assert solve(7, 5, ["10101", "00001", "00110", "11110", "00100", "11111", "10000"]) == 10


if __name__ == "__main__":
    test()
    main()
