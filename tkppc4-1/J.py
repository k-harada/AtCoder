from itertools import chain, combinations


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


N, M = map(int, input().split())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
A_s = sum(A_list)
B_s = sum(B_list)
A_s2 = A_s // 2
B_s2 = B_s // 2

A_pow_list = [sum(sub_a) for sub_a in powerset(A_list) if sum(sub_a) > A_s2][:-1]
B_pow_list = [sum(sub_b) for sub_b in powerset(B_list) if sum(sub_b) > B_s2][:-1]

A_pow_list_s = sorted(A_pow_list)

B_A_sum_list_s = sorted(B_pow_list)
B_B_sum_list_s = [B_s - b for b in B_A_sum_list_s]

LA = len(A_pow_list_s)
LB = len(B_A_sum_list_s)
w_max = 0

right = 0
left = 0

for i in range(LA):
    aa = A_pow_list_s[i]
    ab = A_s - aa
    if right < LB:
        while aa > B_A_sum_list_s[right]:
            right += 1
            if right == LB:
                break
    if left < LB:
        while ab <= B_B_sum_list_s[left]:
            left += 1
            if left == LB:
                break
    w = max(0, right - left)
    if w > w_max:
        w_max = w

print(w_max / LB)
