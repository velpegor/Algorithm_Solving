import sys
input = sys.stdin.readline

dp = [[0] * 4 for _ in range(100001)]
dp[1] = [0,1,0,0]
dp[2] = [0,0,1,0]
dp[3] = [0,1,1,1]

for i in range(4, 100001):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % 1000000009
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % 1000000009
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % 1000000009

n = int(input())
for i in range(n):
    num = int(input())
    print(sum(dp[num]) % 1000000009)