def solve(n, a_list, b_list):
    res = 0
    flag = 0
    state_a = 0
    state_b = 0
    for a, b in zip(a_list, b_list):
        state_a += a
        state_b += b
        if state_a > state_b:
            if flag == -1:
                res += 1
            flag = 1
        elif state_a < state_b:
            if flag == 1:
                res += 1
            flag = -1
    return res


def main():
    res = []
    while True:
        n = int(input())
        if n == 0:
            break
        a_list = list(map(int, input().split()))
        b_list = list(map(int, input().split()))
        res.append(solve(n, a_list, b_list))
    for r in res:
        print(r)


def test():
    assert solve(3, [5, 15, 5], [10, 5, 15]) == 2
    assert solve(9, [
        10, 10, 10, 10, 10, 10, 10, 10, 10
    ], [
        5, 15, 10, 5, 15, 10, 5, 15, 10
    ]) == 0
    assert solve(9, [
        10, 10, 10, 5, 15, 10, 10, 10, 10
    ], [
        5, 15, 10, 10, 10, 10, 5, 15, 10
    ]) == 2


if __name__ == "__main__":
    test()
    main()
