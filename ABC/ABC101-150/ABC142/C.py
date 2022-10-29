def solve_c(n, a_list):
    res_list = [0] * n
    for i in range(n):
        res_list[a_list[i] - 1] = i + 1
    return res_list


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res_list = solve_c(n, a_list)
    print(" ".join([str(r) for r in res_list]))


if __name__ == "__main__":
    main()
