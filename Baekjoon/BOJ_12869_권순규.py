# 뮤탈리스크
from itertools import permutations
N = 0
scv = []
MAX = 25
answer = MAX
dp = [[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)]
arr = list(permutations([1,3,9],3)) # 1,3,9를 나열하는 모든 수열의 조합을 만들어준다. 배열에서 3개 뽑아서 나열한다는 의미

def func(scv1,scv2,scv3):
    
    if scv1 < 0:
        scv1 = 0
    
    if scv2 < 0:
        scv2 = 0
    
    if scv3 < 0:
        scv3 = 0
    
    if scv1 == 0 and scv2 == 0 and scv3 == 0:
        return 0
    
    if dp[scv1][scv2][scv3] != -1:
        return dp[scv1][scv2][scv3]
    
    dp[scv1][scv2][scv3] = MAX
    for i in arr:
        dp[scv1][scv2][scv3] = min(func(scv1-i[0],scv2-i[1],scv3-i[2]),dp[scv1][scv2][scv3])
    dp[scv1][scv2][scv3] += 1 # 각 모든 경우의 수에 대하여 최소를 찾고 거기에 +1을 해줘야 한다.
        
    return dp[scv1][scv2][scv3]

if __name__ == "__main__":
    N = int(input())
    scv = list(map(int,input().split()))
    
    while len(scv) < 3:
        scv.append(0)
        
    print(func(scv[0],scv[1],scv[2]))