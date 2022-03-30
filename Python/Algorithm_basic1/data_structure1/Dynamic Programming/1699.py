n = int(input())
num_double = [i**2 for i in range(317)]
dp = [i for i in range(n+1)]

for i in range(1, n+1):
    for j in num_double:
        if j > i:
            break
        if dp[i] > dp[i - j] + 1:
            dp[i] = dp[i-j]+1
print(dp[n])
