ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def solve(p_list):
    return "".join([ALPHABET[p - 1] for p in p_list])


def main():
    p_list = list(map(int, input().split()))
    res = solve(p_list)
    print(res)


if __name__ == "__main__":
    main()
