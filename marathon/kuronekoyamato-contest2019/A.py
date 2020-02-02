from collections import defaultdict
from heapq import heappush, heappop

# input
n1, n2, n3, n4, n5 = map(int, input().split())

G0 = defaultdict(lambda: defaultdict(lambda: 100000000))
G1 = defaultdict(lambda: defaultdict(lambda: 100000000))

p_dict = dict()
pd_dict = dict()

# input and create graph
for _ in range(n1):
    r, ls, fs = input().split()
    length = int(ls)
    flag = int(fs)
    # for G0
    G0[r + "SES"][r + "SEE"] = length
    if flag == 0:
        G0[r + "ESE"][r + "ESS"] = length
    # for G1
    G1[r + "S"][r + "E"] = length
    G1[r + "E"][r + "S"] = length

for _ in range(n2):
    c, r1, r2 = input().split()
    # for G0
    G0[r1 + r1[-1]][r2 + r2[-2]] = 0
    # for G1
    G1[r1[:-2] + r1[-1]][c] = 0
    G1[c][r1[:-2] + r1[-1]] = 0
    G1[c][r2[:-2] + r2[-2]] = 0
    G1[r2[:-2] + r2[-2]][c] = 0

for i in range(n3):
    p, r, ls = input().split()
    ds = int(ls)

    length = G0[r + "SES"][r + "SEE"]
    de = length - ds

    # for G0
    direction = p[-2:]
    if direction == "SE":
        G0[r + "SES"][p] = ds
        G0[p][r + "SEE"] = de
    else:
        assert G0[r + "ESE"][r + "ESS"] == length
        G0[r + "ESE"][p] = de
        G0[p][r + "ESS"] = ds

    # for G1
    G1[r + "S"][p] = ds
    G1[p][r + "S"] = ds
    G1[r + "E"][p] = de
    G1[p][r + "E"] = de

    # save
    p_dict[p] = r + direction, ds
    pd_dict[p] = r, ds

for i in range(n4):
    d, r, ls = input().split()
    ds = int(ls)

    length = G0[r + "SES"][r + "SEE"]
    de = length - ds

    # for G1
    G1[r + "S"][d] = ds
    G1[d][r + "S"] = ds
    G1[r + "E"][d] = de
    G1[d][r + "E"] = de

    # save
    pd_dict[d] = r, ds

# direct edges
# for G0
for p1 in p_dict.keys():
    r1, ds1 = p_dict[p1]
    direction = r1[-2:]
    for p2 in p_dict.keys():
        r2, ds2 = p_dict[p2]
        if r1 == r2:
            if direction == "SE":
                if ds1 <= ds2:
                    # S p1 p2 E
                    G0[p1][p2] = ds2 - ds1
                else:
                    # S p2 p1 E
                    G0[p2][p1] = ds1 - ds2
            else:
                if ds1 <= ds2:
                    # E p2 p1 S
                    G0[p2][p1] = ds2 - ds1
                else:
                    # E p1 p2 S
                    G0[p1][p2] = ds1 - ds2

# for G1
for d1 in pd_dict.keys():
    r1, ds1 = pd_dict[d1]
    for d2 in pd_dict.keys():
        r2, ds2 = pd_dict[d2]
        if r1 == r2:
            G1[d1][d2] = abs(ds2 - ds1)
            G1[d2][d1] = abs(ds2 - ds1)

D0 = defaultdict(lambda: defaultdict(lambda: -1))
D1 = defaultdict(lambda: defaultdict(lambda: -1))

# solve G0
for p1 in p_dict.keys():
    d_dict = defaultdict(lambda: 100000000)
    d_dict[p1] = 0
    h = []
    heappush(h, (0, p1))

    while len(h) > 0:
        d, p = heappop(h)
        for q in G0[p].keys():
            d_new = d + G0[p][q]
            if d_new < d_dict[q]:
                d_dict[q] = d_new
                heappush(h, (d_new, q))

    for p2 in p_dict.keys():
        if d_dict[p2] < 100000000:
            D0[p1][p2] = d_dict[p2]

# solve G1
for d1 in pd_dict.keys():
    d_dict = defaultdict(lambda: 100000000)
    d_dict[d1] = 0
    h = []
    heappush(h, (0, d1))

    while len(h) > 0:
        d, p = heappop(h)
        for q in G1[p].keys():
            d_new = d + G1[p][q]
            if d_new < d_dict[q]:
                d_dict[q] = d_new
                heappush(h, (d_new, q))

    for d2 in pd_dict.keys():
        if d_dict[d2] < 100000000:
            D1[d1][d2] = d_dict[d2]

for _ in range(n5):
    t, x, y = input().split()
    if t == "0":
        print(D0[x][y])
    else:
        print(D1[x][y])
