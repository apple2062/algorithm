# 반도체 설계 (2352) - 12015번(LIS) 문제와 동일
# 시간 복잡도 : O(N * log N) 


from bisect import bisect_left

def solution(port):
      answer = [0]
      for i in port:
            if answer[-1] < i:
                  answer.append(i)
            elif answer[-1] > i:
                  answer[bisect_left(answer,i)] = i
      return len(answer)-1

n = int(input()) #6
port = list(map(int,input().split())) #[4,2,6,3,1,5]

print(solution(port))



