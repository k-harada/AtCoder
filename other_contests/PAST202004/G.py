from collections import deque


def solve(q, query_list):
    res_list = []
    queue = deque()
    for query in query_list:
        if query[0] == "1":
            queue.append((query[1], int(query[2])))
        else:
            res = 0
            res_dict = dict()
            for s in "qwertyuiopasdfghjklzxcvbnm":
                res_dict[s] = 0
            d = int(query[1])
            while len(queue) > 0:
                c, x = queue.popleft()
                if x < d:
                    res_dict[c] += x
                    d -= x
                elif x == d:
                    res_dict[c] += x
                    break
                else:
                    queue.appendleft((c, x - d))
                    res_dict[c] += d
                    break
            for k in res_dict.keys():
                res += res_dict[k] ** 2
            res_list.append(res)
    return res_list


def main():
    q = int(input())
    query_list = [list(input().split()) for _ in range(q)]
    res = solve(q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(6, [("1", "a", "5"), ("2", "3"), ("1", "t", "8"), ("1", "c", "10"), ("2", "21"), ("2", "4")]) == [
        9, 168, 0
    ]
    assert solve(4, [("1", "x", "5"), ("1", "y", "8"), ("2", "7"), ("1", "x", "8")]) == [29]
    assert solve(3, [("1", "p", "3"), ("1", "q", "100000"), ("2", "100000")]) == [9999400018]


if __name__ == "__main__":
    test()
    main()
