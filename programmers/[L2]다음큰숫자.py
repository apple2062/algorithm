# 다음 큰 숫자 (https://programmers.co.kr/learn/courses/30/lessons/12911)
# format(number, 'b') >> number을 2진수로 변환하여 리턴! 을 활용 

def solution(n):
    temp = list(format(n,'b')).count('1')
    while True:
        n += 1 
        if list(format(n,'b')).count('1') == temp:
            return n
        
