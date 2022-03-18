n = int(input())

def hanoi(n, first, second, third):
    if(n==1):
        print(first, third)
    else:
        hanoi(n-1,first, third, second)
        print(first, third)
        hanoi(n-1, second, first, third)

sum  = 1
for i in range(n-1):
    sum = sum *2 +1
print(sum)
hanoi(n,1,2,3)
