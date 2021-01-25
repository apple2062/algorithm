# 오름세 (3745)
'''
dp 로 해결하였더니 75% 쯤에서 시간초과 났다.
해결 방안 : 이진 탐색으로 해결
'''

from bisect import bisect_left

def solution(stock):
      stack = [0]
      for i in stock:
            if stack[-1] < i:
                  stack.append(i)
            elif stack[-1] > i:
                  stack[bisect_left(stack,i)] = i
      return len(stack)-1

answer = []

while True:
      try:
            n = int(input())  # n일 동안의 주가
            stock = list(map(int, input().split()))
            answer.append(solution(stock))
      except :
            break

for i in answer:
      print(i)


