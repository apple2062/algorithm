# K번째수 (https://www.acmicpc.net/problem/1300 )
# ref : https://claude-u.tistory.com/449
'''
k는 min(109, N2)보다 작거나 같은 자연수 >> 범위 대박 크네

솔직히 이분탐색으로 푸는지 몰랐음..ㅎ
sol ) 이분 탐색으로 어떤 수보다 작은 자연수의 곱(i * j)이 몇 개인지 알아냄
      A보다 작은 숫자가 몇개인지 찾아내면 A가 몇 번째 숫자인지 알 수 있음
'''

def solution(n,k):
    start,end = 1,10**9
    while start<=end:
        mid = (start+end)//2
        temp = 0
        for i in range(1,n+1):
            # 10X10 배열에 20 보다 작거나 같은 수를 찾는다고 할때, 1부터 시작하는 경우 1*1 - 1*10 까지가  10개가 끝이기 때문에 아래를 그냥 mid//i 로 해버리면 10이 아닌 20이 count돼버림
            temp += min((mid//i),n)
        if temp >= k:
            answer = mid
            end = mid-1
        else:
            start = mid+1
    return answer


n = int(input()) # 배열의 크기
k = int(input()) # B를 오름차순 정렬한 후 B[k]값

print(solution(n,k))
