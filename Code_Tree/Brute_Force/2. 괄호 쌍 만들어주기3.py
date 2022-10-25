n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i, n-1):
        for k in range(j, n-2):
            if (arr[i] <= arr[j] and arr[j] < arr[k]):
                cnt +=1

print(cnt)