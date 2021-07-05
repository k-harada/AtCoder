def solve(s):
    if s == '8':
        return 'Yes'
    if len(s) == 2:
        if int(s) % 8 == 0:
            return 'Yes'
        elif (int(s[1]) * 10 + int(s[0])) % 8 == 0:
            return 'Yes'
    # count
    count_list_s = [0] * 10
    for n_ in s:
        count_list_s[int(n_)] += 1
    for i in range(100, 1000):
        if i % 8 == 0:
            count_list_i = [0] * 10
            for j_ in str(i):
                count_list_i[int(j_)] += 1
            flag = 0
            for k in range(10):
                if count_list_i[k] > count_list_s[k]:
                    flag = 1
            if flag == 0:
                return 'Yes'
    return 'No'


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve('1234') == 'Yes'
    assert solve('1333') == 'No'
    assert solve('8') == 'Yes'


if __name__ == "__main__":
    test()
    main()
