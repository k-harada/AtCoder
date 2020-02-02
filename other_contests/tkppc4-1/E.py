N, M, K, E = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list_s = sorted(A_list)
B_list_s = sorted(B_list, reverse=True)

# case Yes
if E + sum(B_list_s[:K]) >= sum(A_list_s):
    res = 0
    R = sum(A_list_s) - E
    for i in range(K):
        R -= B_list_s[i]
        res += 1
        if R <= 0:
            break
    print("Yes")
    print(res)
# case No
else:
    res = 0
    E += sum(B_list_s[:K])
    for i in range(N):
        if E >= A_list_s[i]:
            res += 1
            E -= A_list_s[i]
        else:
            break
    print("No")
    print(res)
