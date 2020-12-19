def solve(h, w, a_list):
    sum_a = sum([sum(a) for a in a_list])
    min_a = min([min(a) for a in a_list])
    return sum_a - min_a * h * w


def main():
    h, w = map(int, input().split())
    a_list = [list(map(int, input().split())) for _ in range(h)]
    res = solve(h, w, a_list)
    print(res)


def test():
    assert solve(2, 3, [[2, 2, 3], [3, 2, 2]]) == 2
    assert solve(3, 3, [[99, 99, 99], [99, 0, 99], [99, 99, 99]]) == 792
    assert solve(3, 2, [[4, 4], [4, 4], [4, 4]]) == 0


if __name__ == "__main__":
    test()
    main()
