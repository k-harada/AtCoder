import numpy as np


def solve(n):
    if n in [1, 2]:
        return np.array([])
    res = np.array([["."] * n for _ in range(n)])
    block_5 = np.array([
        ["a", "a", "b", "b", "c"],
        ["d", "e", "e", ".", "c"],
        ["d", ".", ".", "f", "g"],
        ["h", ".", ".", "f", "g"],
        ["h", "i", "i", "j", "j"]
    ])
    if n == 5:
        return block_5
    if n == 10:
        res[0:5, 0:5] = block_5
        res[5:10, 5:10] = block_5
        return res
    block_3 = np.array([
        ["a", "a", "."],
        [".", ".", "a"],
        [".", ".", "a"]
    ])
    if n % 3 == 0:
        for i in range(0, n, 3):
            res[i:i + 3, i:i + 3] = block_3
        return res
    res_4 = 0
    res_7 = 0
    res_9 = 0
    if n % 4 == 0:
        res_4 = n // 4
    elif (n - 7) % 4 == 0 and n >= 7:
        res_4 = (n - 7) // 4
        res_7 = 1
    elif (n - 14) % 4 == 0 and n >= 14:
        res_4 = (n - 14) // 4
        res_7 = 2
    elif (n - 21) % 4 == 0 and n >= 21:
        res_4 = (n - 21) // 4
        res_7 = 3
    elif n == 13:
        res_4 = 1
        res_9 = 1
    elif n == 17:
        res_4 = 2
        res_9 = 1
    else:
        print(Error)

    block_4 = np.array([
        ["a", "b", "c", "c"],
        ["a", "b", "d", "d"],
        ["e", "e", "f", "g"],
        ["h", "h", "f", "g"],
    ])

    block_7 = np.array([
        [".", ".", "a", "b", "c", ".", "."],
        [".", ".", "a", "b", "c", ".", "."],
        ["d", "d", "e", "e", ".", "f", "f"],
        ["g", "g", ".", ".", "h", "i", "i"],
        ["j", "j", ".", ".", "h", "k", "k"],
        [".", ".", "l", "m", "n", ".", "."],
        [".", ".", "l", "m", "n", ".", "."]
    ])

    block_9 = np.array([
        ["a", "a", "b", "b", "c", "c", ".", ".", "."],
        ["d", "d", "e", "e", "f", "f", ".", ".", "."],
        ["g", "g", "h", "h", "i", "i", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "j", "k", "l"],
        [".", ".", ".", ".", ".", ".", "j", "k", "l"],
        [".", ".", ".", ".", ".", ".", "m", "n", "o"],
        [".", ".", ".", ".", ".", ".", "m", "n", "o"],
        [".", ".", ".", ".", ".", ".", "p", "q", "r"],
        [".", ".", ".", ".", ".", ".", "p", "q", "r"]
    ])

    base = 0
    for i in range(res_4):
        res[base:base + 4, base:base + 4] = block_4
        base += 4
    for i in range(res_7):
        res[base:base + 7, base:base + 7] = block_7
        base += 7
    for i in range(res_9):
        res[base:base + 9, base:base + 9] = block_9
        base += 9

    return res


def main():
    n = int(input())
    res = solve(n)
    if res.shape[0] == 0:
        print(-1)
    else:
        for i in range(res.shape[0]):
            print("".join(list(res[i, :])))


if __name__ == "__main__":
    main()
