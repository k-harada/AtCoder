def solve(n, q, event_list):
    status = [0] * (n + 1)
    res = []
    for k, x in event_list:
        if k == 1:
            status[x] += 1
        elif k == 2:
            status[x] += 2
        else:
            if status[x] >= 2:
                res.append("Yes")
            else:
                res.append("No")
    # print(res)
    return res


def main():
    n, q = map(int, input().split())
    event_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, event_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 9, [
        (3, 1), (3, 2), (1, 2), (2, 1), (3, 1), (3, 2), (1, 2), (3, 2), (3, 3)
    ]) == [
        "No", "No", "Yes", "No", "Yes", "No"
    ]


if __name__ == "__main__":
    test()
    main()
