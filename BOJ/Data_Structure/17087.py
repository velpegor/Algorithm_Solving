def gcd(a, b):
    while b > 0:
        mod = b
        b = a%b
        a = mod
    return a

n, s = map(int, input().split())
arr = list(map(int, input().split()))
min_num = []

for i in range(n):
    min_num.append(abs(s-arr[i]))

d = min(min_num)
for j in range(len(min_num)):
    d = gcd(min_num[j],d)

print(d)
