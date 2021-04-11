# 이진변환 반복하기 (https://programmers.co.kr/learn/courses/30/lessons/70129)
# bin(), oct(), hex() 내장 함수 활용하기


def solution(s):
    stage = 0
    zero = 0
    while s != '1':
        stage += 1
        val = s.count('1')
        zero += len(s)-val
        s = bin(val)[2:]
    return [stage,zero]
    

