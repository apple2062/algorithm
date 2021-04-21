# 숫자의 표현 ( https://programmers.co.kr/learn/courses/30/lessons/12924 )


def solution(n):
    answer = 0
    # 1부터 시작하는 연속되는 합이 n 을 넘어서는 안되므로 연속되는 숫자의 길이를 구하기 위함
    length = 1
    while n*2 >= length*(length+1):
        length += 1 
    
    #구한 길이까지만 돌려보며 연속된 합의 조합을 찾으면 됨
    for i in range(1,length+1):
        val  = n-(i*(i+1)//2)
        if val%i == 0 and val//i!=0:
            answer += 1
    return answer

