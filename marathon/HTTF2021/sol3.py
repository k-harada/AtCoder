from collections import deque


def min_path(board, x, y):
    """
    :param board: list of list
    :param x: 開始地点
    :param y: 開始地点
    :return: 追加すべき点のlist
    """
    r = len(board)
    c = len(board[0])
    d_min = r + c
    i_min = 0
    j_min = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] == 0:
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


def solve_one(n, c0):

    # とりあえず全部埋める
    res = []
    for i in range(n):
        for j in range(n):
            res.append(f'{1} {i} {j}')

    return n * n * c0, res


def solve_sub(n, ij_list, num, block, c0, flag, d_i, d_j):

    nb, mb, cb, s_list = block
    block_arr = [[0] * mb for _ in range(nb)]
    for i in range(nb):
        for j in range(mb):
            if s_list[i][j] == '#':
                block_arr[i][j] = 1

    # とりあえず配置してしまう
    board = [[0] * n for _ in range(n)]
    score = 0
    res = []
    for i in range(d_i, n - nb + 1, nb):
        for j in range(d_j, n - mb + 1, mb):
            res.append(f'{num} {i} {j}')
            score += cb
            for p in range(nb):
                for q in range(mb):
                    board[i + p][j + q] += block_arr[p][q]

    # 上と下を繋ぐコストを計算する
    block_ud = [[0] * mb for _ in range(2 * nb)]
    for p in range(nb):
        for q in range(mb):
            block_ud[p][q] += block_arr[p][q]

    min_len_ud = nb * 2
    min_point_list_ud = []
    for p in range(nb):
        for q in range(mb):
            if block_arr[p][q] == 1:
                point_list = min_path(block_ud, nb + p - 1, q)
                if len(point_list) < min_len_ud:
                    min_len_ud = len(point_list)
                    min_point_list_ud = point_list

    # 左と右を繋ぐコストを計算する
    block_lr = [[0] * (2 * mb) for _ in range(nb)]
    for p in range(nb):
        for q in range(mb):
            block_lr[p][q] += block_arr[p][q]

    min_len_lr = nb * 2
    min_point_list_lr = []
    for p in range(nb):
        for q in range(mb):
            if block_arr[p][q] == 1:
                point_list = min_path(block_lr, p, mb + q - 1)
                if len(point_list) < min_len_lr:
                    min_len_lr = len(point_list)
                    min_point_list_lr = point_list

    # 上下
    for i in range(d_i, n - 2 * nb + 1, nb):
        j = d_j
        for p, q in min_point_list_ud:
            if board[i + p][j + q] == 0:
                res.append(f'{1} {i + p} {j + q}')
                score += c0
                board[i + p][j + q] += 1

    # 左右
    i = d_i
    for j in range(d_j, n - 2 * mb + 1, mb):
        for p, q in min_point_list_lr:
            if board[i + p][j + q] == 0:
                res.append(f'{1} {i + p} {j + q}')
                score += c0
                board[i + p][j + q] += 1

    # 上下のコストと左右のコストを比較 -> 両方やる
    if flag == 1:
        # 上下
        for i in range(d_i, n - 2 * nb + 1, nb):
            for j in range(d_j + mb, n - mb + 1, mb):
                for p, q in min_point_list_ud:
                    if board[i + p][j + q] == 0:
                        res.append(f'{1} {i + p} {j + q}')
                        score += c0
                        board[i + p][j + q] += 1
    else:
        # 左右
        for i in range(d_i + nb, n - nb + 1, nb):
            for j in range(d_j, n - 2 * mb + 1, mb):
                for p, q in min_point_list_lr:
                    if board[i + p][j + q] == 0:
                        res.append(f'{1} {i + p} {j + q}')
                        score += c0
                        board[i + p][j + q] += 1

    # 目標点をboardとつなぐ
    for i, j in ij_list:
        point_list = min_path(board, i, j)
        for p, q in point_list:
            if board[p][q] == 0:
                res.append(f'{1} {p} {q}')
                score += c0
                board[p][q] += 1

    return score, res


def solve(n, k, b, ij_list, block_list):

    c0 = block_list[0][2]
    score, res = solve_one(n, c0)

    for i in range(1, b):
        block = block_list[i]
        for d_i in range(block[0]):
            for d_j in range(block[1]):
                score_sub, res_sub = solve_sub(n, ij_list, i + 1, block, c0, 0, d_i, d_j)
                if score_sub < score:
                    score = score_sub
                    res = res_sub
                score_sub, res_sub = solve_sub(n, ij_list, i + 1, block, c0, 1, d_i, d_j)
                if score_sub < score:
                    score = score_sub
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
