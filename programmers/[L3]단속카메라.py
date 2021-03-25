# https://programmers.co.kr/learn/courses/30/lessons/42884

import sys

def solution(routes):
    answer = 1 #첫 시작에 시시티비 무조건 하나 필요하니까 1부터 시작
    routes.sort()
    start,end = routes[0][0],routes[0][1]
    for i in range(1,len(routes)):
        # 출발 지점이 start와 end사이에 있다면,
        if start <= routes[i][0] <= end :
            # start를 변경해주고
            start = routes[i][0]
            # 이 때, 도착 지점이 end 보다 작다면 start와 end사이에 고속도로가 포함되어 있는 상태이므로
            if routes[i][1] < end :
                # end도 변경
                end = routes[i][1]
        # 출발 지점이 start와 end사이에 벗어나서 존재한다면
        elif end < routes[i][0]:
            # 시시티비 무조건 하나 추가해준뒤, start 와 end를 변경해줌
            answer += 1
            start = routes[i][0]
            end = routes[i][1]
    return answer

routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]] # return 2
print(solution(routes))
