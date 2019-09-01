def solve_e(n, a_list):
    days = 0
    ind_list = [0] * n
    match_count = 0
    queue = list(range(n))
    stack = dict()
    while len(queue) > 0:
        days += 1
        new_queue = []
        for p in queue:
            if ind_list[p] < n - 1:
                q = a_list[p][ind_list[p]] - 1
                k = str(min(p, q)) + "_" + str(max(p, q))
                if k in stack.keys():
                    ind_list[p] += 1
                    ind_list[q] += 1
                    # print(days, p, q)
                    new_queue.append(p)
                    new_queue.append(q)
                    match_count += 1
                else:
                    stack[k] = 1
        queue = new_queue
    if match_count == n * (n - 1) // 2:
        return days - 1
    else:
        return -1


def test():
    N = 1000
    A_list = []
    for i in range(N):
        A_list.append(list(range(1, i + 1)) + list(range(i + 2, N + 1)))
    print(solve_e(N, A_list))


def main():
    N = int(input())
    A_list = []
    for _ in range(N):
        A_list.append(list(map(int, input().split())))
    print(solve_e(N, A_list))


if __name__ == "__main__":
    main()
