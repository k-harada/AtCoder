from collections import Counter

N = int(input())
a_list = list(map(int, input().split()))

res = 'Yes'

a_dict = Counter(a_list)


a_keys = list(a_dict.keys())
if len(a_keys) > 3:
    res = 'No'
elif len(a_keys) == 3:
    a, b, c = a_keys
    if a_dict[a] != a_dict[b]:
        res = 'No'
    if a_dict[a] != a_dict[c]:
        res = 'No'
    if a ^ b != c:
        res = 'No'
    if b ^ c != a:
        res = 'No'
    if c ^ a != b:
        res = 'No'
elif len(a_keys) == 2:
    a, b = a_keys
    if a_dict[a] == 2 * a_dict[b]:
        if b != 0:
            res = 'No'
    elif 2 * a_dict[a] == a_dict[b]:
        if a != 0:
            res = 'No'
    else:
        res = 'No'
else:
    a = a_keys[0]
    if a != 0:
        res = 'No'
print(res)
