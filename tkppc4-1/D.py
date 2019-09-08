N = int(input())
A_list = list(map(int, input().split()))

vec_list = []
for i in range(N - 1):
    if A_list[i + 1] > A_list[i]:
        vec_list.append("up")
    elif A_list[i + 1] < A_list[i]:
        vec_list.append("down")
    if len(vec_list) >= 2:
        if vec_list[-1] == vec_list[-2]:
            trash = vec_list.pop()

if len(vec_list) > 0:
    print(len(vec_list) + 1)
else:
    print(0)
