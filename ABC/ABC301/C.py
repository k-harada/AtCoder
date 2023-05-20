def solve(s, t):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    counter_s = dict()
    counter_t = dict()
    for c in alphabet:
        counter_s[c] = 0
        counter_t[c] = 0
    counter_s["@"] = 0
    counter_t["@"] = 0
    for c in s:
        counter_s[c] += 1
    for c in t:
        counter_t[c] += 1
    res = "Yes"
    for c in alphabet:
        if c in ["a", "t", "c", "o", "d", "e", "r"]:
            if counter_s[c] > counter_t[c]:
                counter_t["@"] -= counter_s[c] - counter_t[c]
            elif counter_s[c] < counter_t[c]:
                counter_s["@"] -= counter_t[c] - counter_s[c]
        else:
            if counter_s[c] != counter_t[c]:
                res = "No"
    if counter_s["@"] < 0 or counter_t["@"] < 0:
        res = "No"
    return res


def main():
    s = input()
    t = input()
    res = solve(s, t)
    print(res)


def test():
    assert solve("ch@ku@ai", "choku@@i") == "Yes"
    assert solve("ch@kud@i", "akidu@ho") == "Yes"
    assert solve("aoki", "@ok@") == "No"
    assert solve("aa", "bb") == "No"


if __name__ == "__main__":
    test()
    main()
