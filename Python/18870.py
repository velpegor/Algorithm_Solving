n = int(input())
arr = list(map(int, input().split()))
arr2=[]

arr2 = list(sorted(set(arr)))

#for문으로 돌리면 시간복잡도가 O(n)이다 => 시간초과뜸
#딕셔너리를 이용하여 시간복잡도  O(1)로 변경
dic = {
    arr2[i] : i for i in range(len(arr2))
}

for i in arr:
    print(dic[i], end= " ")

#문제에서 배열을 중복제거 + 순서정렬을 하면 개수와 똑같은 인덱스 값이 나온다.

