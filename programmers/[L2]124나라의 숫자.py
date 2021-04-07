# 124나라의 숫자 (https://programmers.co.kr/learn/courses/30/lessons/12899)
# ref : https://itholic.github.io/kata-124-world/
'''
# [1,2,4]로만 표현되니까 3진법으로 생각해볼때, 보통 어떤 수 n 을 2진법으로 바꾼다하면 2로 계속 나누면서 1과0을 계산하듯, 
# 주어진 수 N에 대해 계속 3으로 나눠보며
# 3으로 나누었을 때 나머지가 1이면 1
# 3으로 나누엇을 때 나머지가 2이면 2
# 3으로 나누었을 떄 나머지가 0이면 4
# 로 채워주면 되는 형태이다.
'''

def solution(n):
    answer = ''
    lst = '412'
    while n:
        n,b = divmod(n,3)
        answer = lst[b] + answer
        if b == 0:
            n-=1
    return answer

