n, m = map(int, input().split())
solve = []

def BackT(depth):
    if depth == m:
        for i in solve:
            print(i , end =" ")
        print()
        return
    for i in range(1,n+1):
        if i not in solve:
            solve.append(i)
            print(solve)
            BackT(depth + 1)
            print(solve)
            solve.pop()
            print(solve)
'''
Back(depth+1) 를 통해 함수를 호출하게 되면, 이 함수를 호출할 때의 상태 스택이 저장된다. 이 때의 스택을 A라고 하자. 
이 스택에는 depth와 i가 저장된다.

그리고 함수를 호출했으니, 맨 처음의 if문으로 돌아가 depth를 검사하게 된다. 맨 처음에 [1,2]를 출력하게 되면, 
스택A에 저장된 depth와 i가 현재 depth와 i가 된다. 
즉 depth는 1이고, i는 2이다. 그리고 호출했던 지점으로 돌아와 다음 코드인 pop을 처리해준다.

이 과정을 반복한다. 재귀 지점에서 스택의 depth와 i가 어떤 상태로 저장되는 지를 이해해야 한다.

[1,4]까지 출력하고, 위의 과정을 반복해 4를 제거한 후에
depth는 0이 되고, i는 1이 된다. depth=0이고 i=1일 때, 
즉 처음에 result에 1를 추가해 [1]를 만들었던 때로 돌아가는 것이다. 
이 때 계속 함수를 호출하면서 아직 pop코드를 처리하지 않았기 때문에 상태를 저장한 스택이 남아있는 것이다. 
이후 pop을 통해 1를 제거하면 다음 i는 2가 되기 때문에 [2]부터 다시 시작하게 되는 것이다.
'''
BackT(0)
