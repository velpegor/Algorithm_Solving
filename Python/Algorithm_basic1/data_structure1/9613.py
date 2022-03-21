import math

n = int(input())



for i in range(n):
    arr = list(map(int,input().split()))
    gcd_arr = []
    for j in range(1, len(arr)-1):
        for x in range(j+1, len(arr)):
            k = math.gcd(arr[j], arr[x])
            gcd_arr.append(k)
    print(sum(gcd_arr))
