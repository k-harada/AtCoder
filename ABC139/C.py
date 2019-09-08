def main():
    n = int(input())
    h_list = list(map(int, input().split()))

    r = 0
    res = 0
    for i in range(n - 1):
        if h_list[i] >= h_list[i + 1]:
            r += 1
            if r > res:
                res = r
        else:
            r = 0
    print(res)


if __name__ == "__main__":
    main()
