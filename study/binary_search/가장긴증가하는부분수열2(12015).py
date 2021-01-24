# 가장 긴 증가하는 부분 수열 2 (12015번)
# 시간 복잡도 : O(N * log N)

'''
풀이 방법 : 가장 긴 증가하는 부분 수열의 자체 (수열의 값) 를 구하는 게 아니라, just 가장 긴 길이를 구하기만 하면 된다는 점이 핵심.
          1. stack 에 최솟값 하나를 넣고 (like stack[0])
          2. 순서대로 돌며 배열 값 x와 stack[-1] 비교하여 (x > stack[-1]) 이면 append(x) 를 해주지만,
          3. (x < stack[-1]) 인 경우 bisect_left() 를 통해 반환된 배열의 값과 x 를 바꿔치기 해주었음.
             바꿔치기 하는 이유는 , 바꿔주더라도 가장 긴 증가하는 부분 수열의 길이가 변하는 게 아니기 떄문
             실제 수열 자체를 구한다면 말이 안되는 수열이지만, 단지 길이만 구한다는 아이디어 자체로 인해 바꿔줄 수 있는 것임

          참고한 블로그 :  https://suri78.tistory.com/199
'''
from bisect import bisect_left
def solution(a):
      stack = [0]
      for i in a:
            if stack[-1] < i:
                  stack.append(i)
                  #print(stack)
            else:
                  stack[bisect_left(stack,i)] = i
                  #print(stack)
      return len(stack)-1

n = int(input())
a = list(map(int,input().split()))
print(solution(a))
