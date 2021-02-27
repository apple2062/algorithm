 # 팰린드롬? ( https://www.acmicpc.net/problem/10942 )
'''
팰린드롬(palindrome)이란? 앞에서부터 읽으나 뒤에서부터 읽으나 같은 단어를 말한다.
                       'aba'나 'a'와 같은 단어는 팰린드롬이며, 'abaccbcb'나 'anavolimilana'와 같은 단어는 팰린드롬이 아니다 >> 앞뒤가 똑같은 단어
                       
    -> dp 를 활용 (ref)
'''

import sys
input = sys.stdin.readline

n = int(input()) # 자연수의 개수
lst = list(map(int,input().split()))
dp = [[0]*(n) for _ in range(n)] # dp[처음인덱스][끝인덱스]

for i in range(n): # s-e 길이가 1 인 경우
    dp[i][i] = 1

for i in range(n-1): # s-e 길이가 2인 경우
    if lst[i] == lst[i+1]:
        dp[i][i+1] = 1

'''
아래 범위들의 예시) (1,5) 의 팰린드롬을 구하려면 필요한 조건 : 
                조건 1, 1번과 5번이 동일한 값이다.
                조건 2. (2,4) 까지가 팰린드롬이다.
'''
for length in range(2,n): # s-e 길이가 3 이상인 경우, 길이 마다 순회하며 dp
    for j in range(n-length): # 길이 만큼의 순회
        if lst[j] == lst[j+length] and dp[j+1][j+length-1] == 1: # 조건1 과 조건 2 만족 시 , True로 바꿔줌
            dp[j][j+length] = 1

m = int(input()) # 질문 개수

for _ in range(m):
    s,e = map(int,input().split())
    print(dp[s-1][e-1])
