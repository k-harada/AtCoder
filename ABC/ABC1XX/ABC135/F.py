s = input()
t = input()

u = s * (len(t) // len(s) + 2)

t_add = t + "."


def partial_match_table(word):
    table = [0] * (len(word) + 1)
    table[0] = -1
    i, j = 0, 1

    while j < len(word):
        matched = word[i] == word[j]

        if not matched and i > 0:
            i = table[i]
        else:
            if matched:
                i += 1
            j += 1
            table[j] = i

    return table


table_tx = partial_match_table(t_add)

match = [0] * len(s)

i = j = 0
while i < len(u) and j < len(t_add):
    if u[i] == t_add[j]:
        i += 1
        j += 1
    elif j == 0:
        i += 1
    else:
        j = table_tx[j]
    if j == len(t_add) - 1:
        match[(i - j) % len(s)] = 1


# search
searched = [0] * len(s)
longest = 0
infinity = False
for i in range(len(s)):
    if searched[i]:
        continue
    searched[i] = 1
    p = i
    right = 0
    while match[p]:
        right += 1
        p = (p + len(t)) % len(s)
        searched[p] = 1
        if p == i:
            infinity = True
            break
    left = 0
    p = i
    while match[(p - len(t)) % len(s)]:
        left += 1
        p = (p - len(t)) % len(s)
        searched[p] = 1
        if p == i:
            infinity = True
            break
    if left + right > longest:
        longest = left + right

if infinity:
    print(-1)
else:
    print(longest)
