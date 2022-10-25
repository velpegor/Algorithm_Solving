def is_prime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

n = int(input())
arr = list(map(int, input().split()))
count = 0

for i in range(n):
    if arr[i] != 1 and is_prime(arr[i]) == True:
        count += 1

print(count)
