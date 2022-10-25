t = int(input())

dp = [0 for i in range(1000001)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for j in range(4, 1000001):
    dp[j] = (dp[j - 1] + dp[j - 2] + dp[j - 3]) % 1000000009

for i in range(t):
    n = int(input())
    print(dp[n])
