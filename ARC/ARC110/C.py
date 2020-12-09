def solve(n, p_list):

    right_deque = list(reversed(p_list))
    res_list = []
    back = 0
    target = 1
    next_target = 1
    expected = 2
    index_now = 0
    index_left = 0

    while len(right_deque):
        # print(back, target, next_target, expected, index_now, index_left)
        v = right_deque.pop()
        if v == target:
            if back == 0 and len(right_deque) > 0:
                return [-1]
            if len(right_deque) > 0:
                right_deque.append(back)
            target = next_target
            back = 0
            for i in range(index_now, index_left, -1):
                res_list.append(i)
            index_left = index_now
            index_now -= 1

        elif v == expected:
            if back == 0:
                expected += 1
            else:
                return [-1]
        else:
            if back == 0:
                next_target = expected
                back = v
                expected = next_target + 1
            else:
                return [-1]
        index_now += 1
    # print(res_list)
    return res_list


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    for r in res:
        print(r)


def test():
    assert solve(5, [2, 4, 1, 5, 3]) == [2, 1, 4, 3]
    assert solve(5, [5, 4, 3, 2, 1]) == [-1]


if __name__ == "__main__":
    test()
    main()
