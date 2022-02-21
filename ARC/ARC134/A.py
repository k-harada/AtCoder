from bisect import bisect_right


def solve(n, l, w, a_list):
    res = 0
    x = 0
    a_list.append(l)
    while x < l:
        # find next start
        next_start = bisect_right(a_list, x)
        # check if already done
        if next_start > 0:
            if a_list[next_start - 1] > x - w:
                x = a_list[next_start - 1] + w
                continue
        d = (a_list[next_start] - x - 1) // w + 1
        res += d
        x += w * d

    return res


def main():
    n, l, w = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, l, w, a_list)
    print(res)


def test():
    assert solve(2, 10, 3, [3, 5]) == 2
    assert solve(5, 10, 3, [0, 1, 4, 6, 7]) == 0
    assert solve(12, 1000000000, 5, [
        18501490, 45193578, 51176297, 126259763, 132941437, 180230259,
        401450156, 585843095, 614520250, 622477699, 657221699, 896711402
    ]) == 199999992


if __name__ == "__main__":
    test()
    main()
