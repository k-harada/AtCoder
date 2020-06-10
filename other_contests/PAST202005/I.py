def solve(n, q, query_list):
    transpose = 0
    rows = [i for i in range(n + 1)]
    cols = [i for i in range(n + 1)]
    res_list = []
    for query in query_list:
        if query[0] == 1:
            if transpose:
                a, b = query[1], query[2]
                cols[a], cols[b] = cols[b], cols[a]
            else:
                a, b = query[1], query[2]
                rows[a], rows[b] = rows[b], rows[a]
        elif query[0] == 2:
            if transpose:
                a, b = query[1], query[2]
                rows[a], rows[b] = rows[b], rows[a]
            else:
                a, b = query[1], query[2]
                cols[a], cols[b] = cols[b], cols[a]
        elif query[0] == 3:
            transpose = 1 - transpose
        elif query[0] == 4:
            if transpose:
                a, b = query[2], query[1]
            else:
                a, b = query[1], query[2]
            i, j = rows[a], cols[b]
            r = n * (i - 1) + (j - 1)
            res_list.append(r)
    return res_list


def main():
    n = int(input())
    q = int(input())
    query_list = [list(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, query_list)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
