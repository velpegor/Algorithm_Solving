h, m = map(int, input().split())
num = int(input())

for i in range(1, num+1):
    m += 1
    if (m>=60):
        h += 1
        m = 0

print(h, m)
