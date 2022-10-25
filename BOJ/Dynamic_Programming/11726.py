dp = [0] * 1001
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5
dp[5] = 8
n = int(input())

for i in range(6, 1001):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)
