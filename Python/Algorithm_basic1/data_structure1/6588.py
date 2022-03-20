import sys

a = 1000000
arr = [True for _ in range(a)]

#에라토스테네스의 체
for i in range(2, int(a**0.6)):
    if arr[i] == True:
        for j in range(i*2, a, i):
            if arr[j] == True:
                arr[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        for i in range(3, a):
            if arr[i] == True and arr[n-i] == True:
                print(f"{n} = {i} + {n-i}")
                break
