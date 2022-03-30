n = int(input())
input_arr = list(map(int, input().split()))
arr = [input_arr[0]]

for i in range(n-1):
    arr.append(max(arr[i] + input_arr[i+1], input_arr[i+1]))

print(max(arr))
