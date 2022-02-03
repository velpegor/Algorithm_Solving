n, k = map(int,input().split())
arr = [i for i in range(1, n+1)]

kill_arr = []
position = 0

for i in range(n):
    position += k-1
    if position >= len(arr):
        position = position % len(arr)
    kill_arr.append(arr.pop(position))

print("<",', '.join(str(i) for i in kill_arr), '>', sep="")

