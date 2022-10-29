from collections import deque


def solve(h, w, ch, cw, dh, dw, s_list):

    s_arr = [[False] * (w + 4) for _ in range(h + 4)]
    for i, s in enumerate(s_list):
        for j in range(w):
            if s[j] == ".":
                s_arr[i + 2][j + 2] = True

    done_arr = [[False] * (w + 4) for _ in range(h + 4)]

    # heap
    queue = deque()
    res = -1
    # start
    queue.append((0, ch + 1, cw + 1))
    # main
    while len(queue):
        d, i, j = queue.popleft()
        if done_arr[i][j]:
            continue
        done_arr[i][j] = True
        # print(d, i, j)
        if i == dh + 1 and j == dw + 1:
            res = d
            # print("done")
            break
        for i_ in range(i - 2, i + 3):
            for j_ in range(j - 2, j + 3):
                if not done_arr[i_][j_] and s_arr[i_][j_]:
                    diff = abs(i_ - i) + abs(j_ - j)
                    if diff > 1:
                        queue.append((d + 1, i_, j_))
                    else:
                        queue.appendleft((d, i_, j_))
    # print(res)
    return res


def main():
    h, w = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    s_list = []
    for i in range(h):
        s = input()
        s_list.append(s)
    res = solve(h, w, ch, cw, dh, dw, s_list)
    print(res)


def test():
    assert solve(4, 4, 1, 1, 4, 4, ["..#.", "..#.", ".#..", ".#.."]) == 1
    assert solve(4, 4, 1, 4, 4, 1, [".##.", "####", "####", ".##."]) == -1
    assert solve(4, 4, 2, 2, 3, 3, ["....", "....", "....", "...."]) == 0
    assert solve(4, 5, 1, 2, 2, 5, ["#.###", "####.", "#..##", "#..##"]) == 2


def test_large():
    assert solve(1000, 1000, 1, 1, 1000, 1000, ["." * 1000 for _ in range(1000)]) == 0


if __name__ == "__main__":
    test()
    # test_large()
    main()
