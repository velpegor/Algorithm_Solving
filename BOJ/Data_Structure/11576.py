A, B = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

num = 0
answer= []

for i in range(n):
    num += a[-1] * (A**i)
    a.pop(-1)

while num != 0:
    answer.append(str(num % B))
    num //= B

print(" ".join(answer[::-1]))
