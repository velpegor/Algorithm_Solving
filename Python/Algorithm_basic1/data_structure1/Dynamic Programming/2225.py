n, k = map(int, input().split())
dp = [[0] * 201 for i in range(201)]

#dp[n][k]
for i in range(201):
    dp[i][1] = 1

for j in range(2, 201):
    dp[1][j] = j

for i in range(2, 201):
    for j in range(2, 201):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000
        #dp[2][3] = dp[2][2] + dp[1][3]

print(dp[n][k])