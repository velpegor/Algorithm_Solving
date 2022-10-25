import sys

arr = list(sys.stdin.readline().strip())
right_arr = []
n = int(input())

for i in range(n):
    command = sys.stdin.readline()

    if command[0] == 'P':
        arr.append(command[2])
    elif command[0] == 'B':
        if len(arr) == 0:
            continue
        else:
            arr.pop()
    elif command[0] == 'L':
        if len(arr) == 0:
            continue
        else:
            right_arr.append(arr.pop())
    else:
        if len(right_arr) == 0:
            continue
        else:
            arr.append(right_arr.pop())

right_arr.reverse()
result_arr = arr + right_arr

for i in result_arr:
    print(i, end='')
