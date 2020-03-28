from collections import deque


def solve(h, w, s_list):
    # cost_map
    cost = [[1000] * w for _ in range(h)]
    cost[0][0] = 0
    # find how many flip
    queue = deque([(0, 0)])
    while len(queue) > 0:
        i, j = queue.popleft()
        if i < h - 1:
            if s_list[i][j] != s_list[i + 1][j]:
                new_cost = cost[i][j] + 1
            else:
                new_cost = cost[i][j]
            if new_cost < cost[i + 1][j]:
                cost[i + 1][j] = new_cost
                queue.append((i + 1, j))
        if j < w - 1:
            if s_list[i][j] != s_list[i][j + 1]:
                new_cost = cost[i][j] + 1
            else:
                new_cost = cost[i][j]
            if new_cost < cost[i][j + 1]:
                cost[i][j + 1] = new_cost
                queue.append((i, j + 1))

    res = (cost[h - 1][w - 1] + 1) // 2
    # print(cost)
    # black-black not admitted
    if s_list[0][0] == "#" and s_list[h - 1][w - 1] == "#":
        res += 1
    return res


def main():
    h, w = map(int, input().split())
    s_list = [list(input()) for _ in range(h)]
    res = solve(h, w, s_list)
    print(res)


def test():
    assert solve(3, 3, [[".", "#", "#"], [".", "#", "."], ["#", "#", "."]]) == 1
    assert solve(2, 2, [["#", "."], [".", "#"]]) == 2


if __name__ == "__main__":
    test()
    main()
