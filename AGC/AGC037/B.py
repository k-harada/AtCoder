N = int(input())
S = list(input())

LARGE = 998244353

res = 1

cnt_dict = dict()
cnt_dict["R"] = 0
cnt_dict["G"] = 0
cnt_dict["B"] = 0
cnt_dict["GB"] = 0
cnt_dict["BR"] = 0
cnt_dict["RG"] = 0

heap_dict = dict()
heap_dict["GB"] = []
heap_dict["BR"] = []
heap_dict["RG"] = []

inverse = {"R": "GB", "G": "BR", "B": "RG"}

for i in range(3*N):

    # input
    cnt_dict[S[i]] += 1

    if cnt_dict[inverse[S[i]]] > 0:
        res *= heap_dict[inverse[S[i]]].pop() * cnt_dict[inverse[S[i]]]
        res %= LARGE
        cnt_dict[S[i]] -= 1
        cnt_dict[inverse[S[i]]] -= 1
    elif cnt_dict["R"] * cnt_dict["G"] > 0:
        if S[i] == "R":
            heap_dict["RG"].append(cnt_dict["G"])
        else:
            heap_dict["RG"].append(cnt_dict["R"])
        cnt_dict["RG"] += 1
        cnt_dict["R"] -= 1
        cnt_dict["G"] -= 1
    elif cnt_dict["B"] * cnt_dict["R"] > 0:
        if S[i] == "B":
            heap_dict["BR"].append(cnt_dict["R"])
        else:
            heap_dict["BR"].append(cnt_dict["B"])
        cnt_dict["BR"] += 1
        cnt_dict["B"] -= 1
        cnt_dict["R"] -= 1
    elif cnt_dict["G"] * cnt_dict["B"] > 0:
        if S[i] == "G":
            heap_dict["GB"].append(cnt_dict["B"])
        else:
            heap_dict["GB"].append(cnt_dict["G"])
        cnt_dict["GB"] += 1
        cnt_dict["G"] -= 1
        cnt_dict["B"] -= 1

if __name__ == "__main__":
    for i in range(1, N+1):
        res *= i
        res %= LARGE
    print(res)
