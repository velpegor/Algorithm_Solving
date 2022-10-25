arr = list(input())
length = len(arr)

cnt = 0
for i in range(length):
    for j in range(i, length-1):
        if arr[i] =='(' and arr[j+1] == ')':
            cnt +=1

print(cnt)
