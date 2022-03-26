N = int(input())

p = [0] + list(map(int,input().split()))
d = [False for _ in range(N+1)]

for i in range(1, N+1):
    for k in range(1, i+1):
        if d[i] == False :
            d[i] = d[i-k]+p[k]
        else :
            d[i] = min(d[i], d[i-k]+p[k])

print(d[N])