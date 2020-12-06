import sys

def bomb(current):
    
    for i in graph[current]:
        if not destroyed[i]:
            return
    
    candidates.append(current)

def fire(current):
    answer_destroyed[current] = True
    for i in graph[current]:
        answer_destroyed[i] = True
        
if __name__ == "__main__":
    numofCities, numofRoads = map(int,input().split())
    graph = [[] for _ in range(numofCities+1)]
    destroyed = [False] * (numofCities+1)
    answer_destroyed = [False] * (numofCities+1)
    
    candidates = []
    cnt = 0
    
    for _ in range(numofRoads):
        a, b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        
    K = int(input())
    destroyedlist = list(map(int,sys.stdin.readline().split()))
    
    for i in destroyedlist:
        destroyed[i] = True
    
    for i in destroyedlist:
        bomb(i)
    
    if candidates:
        cnt = 0
        for i in candidates:
            cnt += 1
            fire(i)
        
        flag = True
        for i in range(1,numofCities+1):
            if answer_destroyed[i] != destroyed[i]:
                flag = False
                break
        if flag:
            print(cnt)                
            for i in candidates:
                print(i,end=' ')
        else:
            print(-1)    
            
    else:
        print(-1)

'''
지도와 같은 모양이 나오지 않을 경우를 판정하는게 어려웠던 문제
문제를 꼼꼼하게 읽지 않았던 것 같다.
자신노드와 모든 인접 노드들이 파괴되었다고 무조건 답이 되는게 아님
예를들어
1-2
3-4-5-6
그래프가 이렇게 있는데 파괴된 도시가 1,2,4,5이면
답은 -1이 되어야 한다.
하지만 1번을 후보에 넣어버리고 이걸 그대로 답으로 하게 되면 틀리게 된다.
그래서 해결방법은
1. K 밑의 배열을 destroyed[배열 원소] = True라고 설정
2. 자신노드와 모든 인접 노드들이 파괴되었으면 그걸 폭탄 후보로 넣음, K개의 도시만큼 반복함
3. 폭탄 후보들을 새로운 destroyed 배열에 표시하면서 폭탄을 터뜨림
4. 처음의 destroyed 배열과 새로운 destroyed 배열이 일치하지 않으면 실패
5. 실패 안했으면 폭탄 후보의 길이와 폭탄 후보들을 출력한다.

'''