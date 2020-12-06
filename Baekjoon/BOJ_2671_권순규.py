'''
- 크게 만들기
- https://www.acmicpc.net/problem/2812
- 그리디 알고리즘, 스택

- 핵심 아이디어:
    - 스택에 가장 N자리의 숫자를 넣는다.
    - 주어진 N자리 숫자를 (N-1)자리부터 순회하면서 스택의 top에 있는 수랑 비교한다.
    - stack에 원소가 존재하고 top에 있는 수가 현재의 수보다 클 때까지 stack에서 pop을 하고 K값을 1 감소시킨다.
    - 현재의 수를 stack에 삽입한다.
    - 이걸 1의 자리 수까지 반복한다.
    - 위 과정 이후 K가 0보다 클 경우, stack에 있는 수를 작은 자리수부터 K번만큼 지우면 된다.
    - 최종 남은 stack을 출력한다.
    - 시간복잡도는 O(N)이 된다.
'''

import sys
N, K = map(int,sys.stdin.readline().split())
num = sys.stdin.readline().strip()

stack = [num[0]]

for i in range(1,len(num)):
    while K and stack[-1] < num[i]:
        stack.pop()
        K -= 1
        if not stack:
            break
        
    stack.append(num[i])
    

for _ in range(K):
    stack.pop()

print(''.join(stack))