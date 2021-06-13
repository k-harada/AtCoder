def solve(n):
    if n == 1:
        return [1, 1]
    fib = [0, 1]
    s = 1
    while s < n:
        s = fib[-1] + fib[-2]
        fib.append(s)
    x = n
    pick_list = []
    for i in range(len(fib) - 1, 0, -1):
        if x >= fib[i]:
            x -= fib[i]
            pick_list.append(i)
    pick_list = list(reversed(pick_list))
    # print(pick_list)
    res_list = []
    d = pick_list[-1]
    e = pick_list.pop()
    while d > 1:
        if e == d:
            res_list.append(2 - d % 2)
            if len(pick_list):
                e = pick_list.pop()
        # 1 -> 4 -> 3 -> 4 -> 3 -> 4 -> 3 ...
        # 2 -> 3 -> 4 -> 3 -> 4 -> 3 -> 4 ...
        if d % 2 == 1:
            res_list.append(4)
        else:
            res_list.append(3)
        d -= 1
    # print(res_list)
    return [len(res_list)] + res_list


def main():
    n = int(input())
    res = solve(n)
    for r in res:
        print(r)


def test():
    assert solve(4) == [5, 2, 3, 4, 2, 3]


if __name__ == "__main__":
    test()
    main()
