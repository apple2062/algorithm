# 이진변환 반복하기 (https://programmers.co.kr/learn/courses/30/lessons/70129)

def solution(s):
    answer = []
    zero =  0
    stage = 0
    while int(s) != 1:
        one = s.count("1")
        zero += (len(s)-one)
        val = ''
        # 이진 변환 
        while one != 0:
            if one % 2 == 0:
                val = '0'+ val
            elif one%2 == 1:
                val = '1'+ val
            one = one//2
        s = val
        stage += 1
    answer.append(stage)
    answer.append(zero)
    return answer
