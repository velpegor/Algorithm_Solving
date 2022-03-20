arr = input()
arr2 = []

for i in range(0,len(arr)):
    arr2.append(arr[i:])

arr2.sort()
for i in arr2:
    print(i)