a, b = map(int,input().split())

INT_MAX = 10000
arr = [0 for i in range(INT_MAX)]

for a in range(a):
    position, al = input().split()
    arr[int(position)-1] = al

max_point = 0
for i in range(0,INT_MAX-b):
    point = 0
    for j in range(i, i+b+1):
        if (arr[j] == 'G'):
            point += 1
        elif (arr[j] == 'H'):
            point += 2
    max_point = max(max_point, point)
print(max_point)