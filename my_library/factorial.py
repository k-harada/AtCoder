MOD = 10 ** 9 + 7

size = 10000
factorial = [1] * (size + 1)
factorial_inv = [1] * (size + 1)
for i in range(1, size + 1):
    factorial[i] = (factorial[i - 1] * i) % MOD

factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)

for i in range(size, 0, -1):
    factorial_inv[i - 1] = (factorial_inv[i] * i) % MOD

if __name__ == "__main__":
    print(factorial[:5])
    print(factorial_inv[:5])
