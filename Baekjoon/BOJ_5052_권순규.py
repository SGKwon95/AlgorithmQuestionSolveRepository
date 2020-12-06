def trie(num):
    d = 0
    flag = False
    for i in num:
        if not visited[d][int(i)]:
            flag = True
            visited[d][int(i)] = True
        d += 1
    
    if not flag:
        return False
    else:
        return True

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        lst = []
        
        for _ in range(n):
            lst.append(input())
        
        lst.sort(key=lambda x:-len(x))
        
        visited = [[False] * 10 for _ in range(10000)]
        flag = False
        for i in lst:
            if not trie(i):
                flag = True
                break
        if flag:
            print('NO')
        else:
            print('YES')