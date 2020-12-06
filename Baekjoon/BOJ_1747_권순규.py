#소수&팰린드롬

def isPalindrome(N):
    length = len(N)
    if length <= 1:
        return True
    
    if N[0] == N[length-1]:
        return isPalindrome(N[1:length-1])
    else:
        return False
    
def isPrime(N):
    for i in range(2,N):
        if N%i == 0:
            return False
    
    return True
        
if __name__ == "__main__":
    answer = int(input())
    if answer == 1:
        print(2)
    else:    
        while True:
            if isPalindrome(str(answer)) and isPrime(answer):
                break
            answer += 1
        
        print(answer)
            