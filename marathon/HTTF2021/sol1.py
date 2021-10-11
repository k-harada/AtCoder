def solve(n, k, b, ij_list, block_list):

    # とりあえず全部埋める
    res = []
    for i in range(n):
        for j in range(n):
            res.append(f'{1} {i} {j}')

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
