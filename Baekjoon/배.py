'''
https://www.acmicpc.net/problem/1092
'''
import sys
N = int(input())
limit = list(map(int,input().split()))
limit.sort(key=lambda x:-x)
M = int(input())
weight = list(map(int,input().split()))
weight.sort()
answer = 0

while True:
    flag = False
    stack=[]
    for i in limit:
        for index in range(-1,-len(weight)-1,-1):
            if weight[index] <= i:
                del weight[index]
                flag = True
                if not weight:
                    answer += 1
                    print(answer)
                    sys.exit(0)
                break
                
    if flag:
        answer += 1
    else:
        break
    
if weight:
    print(-1)
else:
    print(answer)

