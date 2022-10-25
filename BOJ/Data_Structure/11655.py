arr = list(input())
arr2 = ""
for i in range(len(arr)):
    if 'A' <= arr[i] <= 'Z':
        if arr[i] <= 'M':
            arr2 += (chr(ord(arr[i])+13))
        else:
            arr2 += (chr(ord(arr[i])-13))
    elif 'a' <= arr[i] <= 'z':
        if arr[i] <= 'm':
            arr2 += (chr(ord(arr[i]) + 13))
        else:
            arr2 += (chr(ord(arr[i]) - 13))
    else:
        arr2 += (arr[i])



print(arr2)
