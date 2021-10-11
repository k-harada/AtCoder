from collections import deque
import numpy as np


def solve_one(n, c0):

    # とりあえず全部埋める
    res = []
    for i in range(n):
        for j in range(n):
            res.append(f'{1} {i} {j}')

    return n * n * c0, res


def min_path(board, x, y):
    """
    :param board: np.array
    :param x: 開始地点
    :param y: 開始地点
    :return: 追加すべき点のlist
    """
    r, c = board.shape
    d_min = r + c
    i_min = 0
    j_min = 0
    for i in range(r):
        for j in range(c):
            if board[i, j] == 0:
                continue
            d = abs(i - x) + abs(j - y)
            if d < d_min:
                d_min = d
                i_min = i
                j_min = j
    point_list = []
    for i in range(min(i_min, x), max(i_min, x) + 1):
        if i == i_min and y == j_min:
            continue
        point_list.append((i, y))
    for j in range(min(j_min, y) + 1, max(j_min, y)):
        point_list.append((i_min, j))

    return point_list


def solve_sub(n, ij_list, block, c0):

    nb, mb, cb, s_list = block

    # 十字を作る
    block_array = np.zeros((nb, mb), dtype=np.int32)
    for i in range(nb):
        for j in range(mb):
            if s_list[i][j] == '#':
                block_array[i, j] = 1

    # 上と下を繋ぐ。上のブロックの下部に負荷を押し付ける
    # これが最善ではないこともある

    min_len = 10000
    min_point_list = []
    for j in range(mb):
        if s_list[0][j] == '#':
            point_list = min_path(block_array, nb - 1, j)
            if len(point_list) < min_len:
                min_len = len(point_list)
                min_point_list = point_list

    # 左と右を繋ぐ。左のブロックの右側に負荷を押し付ける
    #


    board = np.zeros((50, 50), dtype=np.int32)

    res = []
    for i in range(n):
        for j in range(n):
            res.append(f'{1} {i} {j}')

    return res


def solve(n, k, b, ij_list, block_list):

    c0 = block_list[0][2]
    score, res = solve_one(n, c0)

    for i in range(1, b):
        block = block_list[i]
        score_sub, res_sub = solve_sub(n, ij_list, block, c0)
        if score_sub < score:
            res = res_sub

    return res


def main():
    n, k, b = map(int, input().split())
    ij_list = [tuple(map(int, input().split())) for _ in range(k)]
    block_list = []
    for _ in range(b):
        n_, m_, c_ = map(int, input().split())
        s_list = [input() for _ in range(n_)]
        block_list.append((n_, m_, c_, s_list))
    res = solve(n, k, b, ij_list, block_list)
    print(len(res))
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
