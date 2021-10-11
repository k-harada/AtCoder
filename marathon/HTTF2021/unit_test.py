import numpy as np


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


if __name__ == "__main__":
    print(min_path(np.array([[0, 1, 0, 0], [0, 1, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0]]), 0, 0))
    print(min_path(np.array([[0, 1, 0, 0], [0, 1, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0]]), 0, 3))
    print(min_path(np.array([[0, 1, 0, 0], [0, 1, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0]]), 1, 1))
