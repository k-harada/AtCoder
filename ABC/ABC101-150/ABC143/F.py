from collections import Counter


def solve_f(n, a_list):
    counts = list(sorted(list(Counter(a_list).values()), reverse=True))
    print(counts)
    return 0


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve_f(n, a_list)
    print(res)


if __name__ == "__main__":
    main()
