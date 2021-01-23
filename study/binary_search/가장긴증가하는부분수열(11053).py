# 가장 긴 증가하는 부분 수열 (11053번)
# 시간 복잡도 : O(N^2)

'''
12015번 풀려다 보니 같은 문제로 n의 범위를 달리하여 난이도를 낮춘 11053 번도 있길래..
그런데 처음에 문제 자체에 도대체 어떤 알고리즘으로 접근해야 하나 감이 전혀 안왔다...
느낌상 딱 dp 같은데 dp 문제 연습이 안되어있어 그런가 접근 자체가 어려웠음 ..ㅜ dp 풀어야겠다..
해결 방안 :  1. dp[i]의 값을 1로 초기화
          2. 현재 위치(i)보다 이전에 있는 원소(j)가 작은지 확인한다. (크거나 같으면 가장 긴 증가하는 부분 수열이 될 수 없음)
          3. 작다면, 현재 위치의 이전 숫자 중, dp 최댓값을 구하고 그 길이에 1을 더해주면 된다.
'''
def solution(a):
      count_num = [1 for _ in range(len(a))]
      for i in range(len(a)):
            for j in range(i):
                  if a[i] > a[j]:
                        count_num[i] = max(count_num[j],count_num[j]+1)
      return max(count_num)

n= int(input()) # 수열 a 의 길이
a = list(map(int,input().split()))

print(solution(a))
