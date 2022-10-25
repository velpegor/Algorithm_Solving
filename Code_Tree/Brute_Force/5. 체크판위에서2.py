a, b = map(int,input().split())
arr = list(map(int,input().split()))

max_cnt = 0
for i in range(a-b+1):
    sum = 0
    for j in range(i,i+b):
        sum += arr[j]
    max_cnt = max(max_cnt, sum)

print(max_cnt)
