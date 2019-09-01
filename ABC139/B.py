A, B = map(int, input().split())
# 1 + R * (A - 1) >= B

if __name__ == "__main__":
    print((B - 1 + A - 2) // (A - 1))
