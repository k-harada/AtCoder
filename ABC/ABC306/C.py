def solve(n, a_list):
    counter = [0] * (n + 1)
    res = []
    for a in a_list:
        counter[a] += 1
        if counter[a] == 2:
            res.append(a)
    return " ".join([str(a) for a in res])


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
