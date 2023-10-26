def solve(n, a_list):
    count = [0] * (n + 1)
    res_pair = []
    for i, a in enumerate(a_list):
        count[a] += 1
        if count[a] == 2:
            res_pair.append((i, a))
    res_pair = list(sorted(res_pair, key=lambda x: x[0]))
    res = " ".join([str(a) for i, a in res_pair])
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [1, 1, 3, 2, 3, 2, 2, 3, 1]) == "1 3 2"
    assert solve(1, [1, 1, 1]) == "1"
    assert solve(4, [2, 3, 4, 3, 4, 1, 3, 1, 1, 4, 2, 2]) == "3 4 1 2"


if __name__ == "__main__":
    test()
    main()
