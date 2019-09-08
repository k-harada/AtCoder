# python3

cnt = 0

test = False
# test = True

if test:
    N = 6000
    import random
    while True:
        answer_1 = random.randint(1, N)
        answer_2 = random.randint(1, N)
        if answer_1 == answer_2:
            continue
        break
    print(N, answer_1, answer_2)
else:
    N = int(input())


def string_2(a, b):
    return " ".join(["?", str(b - a + 1)] + [str(v) for v in range(a, b + 1)])


def string_1_1(a, b, c, d):
    abcd_list = [str(v) for v in range(a, b + 1)] + [str(v) for v in range(c, d + 1)]
    return " ".join(["?", str(len(abcd_list))] + abcd_list)


def query_string(s):
    if test:
        s_list = list(s.split())[2:]
        if str(answer_1) in s_list and str(answer_2) in s_list:
            return "Rabbit"
        else:
            return "Human"
    else:
        print(s, flush=True)
        r = input().rstrip()
        return r


def commit_string(s):
    print(s, flush=True)


status = 2
a = 1
b = N
c = -1
d = -1

while status == 2:
    # two in [a, b]
    if b == a + 1:
        # end
        res_string = " ".join(["!", str(a), str(b)])
        status = 0
    elif b == a + 2:
        res_string = " ".join(["?", "2", str(a), str(a + 1)])
        cnt += 1
        res = query_string(res_string)
        if res == "Rabbit":
            res_string = " ".join(["!", str(a), str(a + 1)])
            status = 0
        else:
            res_string = " ".join(["?", "2", str(a), str(a + 2)])
            cnt += 1
            res = query_string(res_string)
            if res == "Rabbit":
                res_string = " ".join(["!", str(a), str(a + 2)])
                status = 0
            else:
                res_string = " ".join(["!", str(a + 1), str(a + 2)])
                status = 0
    else:
        if cnt == 0 and b > 4096:
            e = 4096
        else:
            e = (a + b) // 2
        res_string = string_2(a, e)
        cnt += 1
        res = query_string(res_string)
        if res == "Rabbit":
            b = e
        else:
            res_string = string_2(e + 1, b)
            cnt += 1
            res = query_string(res_string)
            if res == "Rabbit":
                a = e + 1
            else:
                status = 1
                d = b
                c = e + 1
                b = e

while status == 1:
    # one in [a, b] and one in [c, d]
    if a < b:
        m = (a + b) // 2
        res_string = string_1_1(a, m, c, d)
        cnt += 1
        res = query_string(res_string)
        if res == "Rabbit":
            b = m
        else:
            a = m + 1
    elif c < d:
        n = (c + d) // 2
        res_string = string_1_1(a, b, c, n)
        cnt += 1
        res = query_string(res_string)
        if res == "Rabbit":
            d = n
        else:
            c = n + 1
    else:
        res_string = " ".join(["!", str(a), str(c)])
        status = 0

if test:
    print(cnt)
commit_string(res_string)
