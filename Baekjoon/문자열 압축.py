# 프로그래머스
# 카카오 2020 기출문제
def solution(s):
    answer = len(s)

    for i in range(1,len(s)):
        tmp = ''
        cnt = 1
        for j in range(0,len(s),i):
            if s[j:j+i] == s[j+i:j+i+i]:
                cnt += 1
            else:
                if cnt != 1:
                    tmp += str(cnt)
                    cnt = 1
                tmp += s[j:j+i]
        #print(tmp)
        answer = min(answer, len(tmp))
        

    return answer

print(solution('aabbaccc'))