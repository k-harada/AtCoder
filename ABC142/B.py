def main():
    n, k = map(int, input().split())
    h_list = list(map(int, input().split()))
    res = 0
    for h in h_list:
        if h >= k:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
