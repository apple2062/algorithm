#1이될때까지
def solution(n,k):
    cnt = 0
    while True:
        if n == 1:
            return cnt
        if n%k != 0:
            n -= 1
            cnt+=1
        else:
            n //= k
            cnt +=1
    return 0

n,k = map(int,input().split())
print(solution(n,k))
