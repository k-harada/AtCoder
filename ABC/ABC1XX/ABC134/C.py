N = int(input())
A_list = [0] * N

for i in range(N):
    A_list[i] = int(input())

A_list_sorted = sorted(A_list)

M1 = A_list_sorted[-1]
M2 = A_list_sorted[-2]

for i in range(N):
    if A_list[i] == M1:
        print(M2)
    else:
        print(M1)
