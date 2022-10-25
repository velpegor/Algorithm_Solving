dic = input()
arr = [0] * 26

for i in dic:
    arr[ord(i) -97]+=1

print(*arr)
