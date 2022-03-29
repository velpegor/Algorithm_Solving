n = int(input())
dp = [0, 1, 1, 2, 3, 5]


for i in range(6, 91):
    result = dp[i-1] + dp[i-2]
    dp.append(result)

print(dp[n])
