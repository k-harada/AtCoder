char_to_ind = dict()
ind_to_char = dict()
for i, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    char_to_ind[char] = i
    ind_to_char[i] = char


def solve(n, s):
    return "".join([ind_to_char[(char_to_ind[c] + n) % 26] for c in s])


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(2, "ABCXYZ") == "CDEZAB"
    assert solve(0, "ABCXYZ") == "ABCXYZ"
    assert solve(13, "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "NOPQRSTUVWXYZABCDEFGHIJKLM"


if __name__ == "__main__":
    test()
    main()
