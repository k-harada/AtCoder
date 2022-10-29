from heapq import heappush, heappop
from collections import deque


def solve(q, query_list):
    h = []
    queue = deque()
    res_list = []
    for query in query_list:
        if query[0] == 1:
            queue.append(query[1])
        elif query[0] == 2:
            if len(h):
                res_list.append(heappop(h))
            else:
                res_list.append(queue.popleft())
        else:
            while len(queue):
                heappush(h, queue.pop())
    # print(res_list)
    return res_list


def main():
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(8, [(1, 4), (1, 3), (1, 2), (1, 1), (3, ), (2, ), (1, 0), (2, )]) == [1, 2]
    assert solve(9, [(1, 5), (1, 5), (1, 3), (2, ), (3, ), (2, ), (1, 6), (3, ), (2, )]) == [5, 3, 5]


if __name__ == "__main__":
    test()
    main()
