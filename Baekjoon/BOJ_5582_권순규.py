def func(long, short):
    N = len(short)
    for start in range(N):
        for end in range(start+size,N):
            compare(long,short,start,end)

def compare(apply, target,start,end):
    global answer
    N = len(apply)
    M = len(target)
    for i in range(N-M):
        flag = True
        for j in range(M):
            if apply[i+j] != target[j]:
                flag = False
                break
        if flag:
            if M > answer:
                answer = M
                size = M+1
            return True
    return False        


if __name__ == "__main__":
    answer = 
    A = input()
    B = input()
    if len(A) > len(B):
        func(A,B)
    else:
        func(B,A)
    print(answer)