S = list(input())
char_before = S[0]
cnt_temp = 1
cnt_list = []

for i in range(1, len(S)):
    if char_before == S[i]:
        cnt_temp += 1
    else:
        cnt_list.append(cnt_temp)
        char_before = S[i]
        cnt_temp = 1
cnt_list.append(cnt_temp)

res = 0
for i in range(len(cnt_list) - 1):
    k = cnt_list[i] // 3
    r = cnt_list[i] % 3
    res += 2 * k + r
    if r == 2:
        cnt_list[i + 1] -= 1

k = cnt_list[-1] // 3
r = cnt_list[-1] % 3
res += 2 * k + r
if r == 2:
    res -= 1

if __name__ == "__main__":
    print(res)
