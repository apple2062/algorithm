# 구명보트 ( https://programmers.co.kr/learn/courses/30/lessons/42885#qna )
# pop,del,remove를 쑤는 순간 효율성 불통 되어 버렸다...ㅠㅠㅠ 애초에 그렇게 접근하면 안되고
# 핵심은 indexing 으로의 접근이었다!!!


def solution(people, limit):
    answer = 0
    #맨 앞, 맨 뒤 더했을 때 구출 가능하면 그렇게 빼고
    #못빼면 뒤에 하나만 빼고
    people.sort()
    start , end = 0, len(people)-1
    while start <= end:
        if people[start] + people[end] <= limit:
            answer+=1
            start+=1
            end-=1
        else:
            end-=1
            answer+=1
    return answer   
