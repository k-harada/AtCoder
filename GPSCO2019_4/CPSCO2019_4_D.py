
N, K = map(int, input().split())
a_list = list(map(int, input().split()))

boring_list = []
straight = 0
c = a_list[0]

for i in range(N):
    # continue
    if a_list[i] == c:
        straight += 1
    # new
    else:
        boring_list.append(straight)
        straight = 1
        c = a_list[i]
# last
boring_list.append(straight)


# binary search whether can or not
def boring(k):
    r_total = 0
    for b in boring_list:
        r = (b + 1) // (k + 1) - 1
        if (b + 1) % (k + 1) != 0:
            r += 1
        r_total += r

    if r_total <= K:
        return True
    else:
        return False

left = 1
right = N
center = 1
while True:

    if boring(center):
        center, right = (left + right) // 2, center
    else:
        left, center = center, (left + right) // 2

    if right == 1:
        break
    if left == right:
        break
    if left == right - 1:
        break

print(right)
