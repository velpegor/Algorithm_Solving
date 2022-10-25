n = int(input())

prime = [True for i in range(1000001)]
prime[0] = prime[1] = False
for i in range(2, 1001):
    for j in range(i*2, 1000001, i):
        prime[j] = False

for i in range(n):
    count = 0
    num = int(input())
    for j in range(2, int(num/2)+1):
        if prime[j] and prime[num-j]:
            count += 1

    print(count)
