# 答えみた

N = int(input())
a_list = list(map(int, input().split()))
LARGE = 10**9 + 7


# cumsum
b_list = [0] * N
b = 0

for i in range(N):
    a = a_list[i]
    b = a ^ b
    b_list[i] = b

v_all_dict = dict()
for b in b_list:
    v_all_dict[b] = [0, 0, 1]

zeros = 0



for i in range(N):

    b = b_list[i]

    t = v_all_dict[b][0]

    # new b
    if t < zeros:
        v_all_dict[b][2] = (v_all_dict[b][2] + v_all_dict[b][1] * (zeros - t)) % LARGE
        v_all_dict[b][0] = zeros

    # up
    v_all_dict[b][1] = (v_all_dict[b][1] + v_all_dict[b][2]) % LARGE

    # zeros
    if b == 0:
        zeros += 1

# res
if b_list[-1] == 0:
    res = 0
    for v in v_all_dict.keys():
        if v != 0:
            res = (res + v_all_dict[v][1]) % LARGE
        else:
            res = (res + 2 ** (zeros - 1) - 1) % LARGE
    res += 1

else:
    v = b_list[-1]
    res = v_all_dict[v][2]

print(res % LARGE)
