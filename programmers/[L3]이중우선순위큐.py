# https://programmers.co.kr/learn/courses/30/lessons/42628

# I 숫자 : 큐에 주어진 숫자를 삽입합니다.
# D 1   : 큐에서 최댓값을 삭제합니다.
# D -1	: 큐에서 최솟값을 삭제합니다.
# 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현.
# 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시
import heapq

def solution(operations):
    answer = []
    oper = []
    for i in operations:
        command, num = i.split()
        if command == 'I':
            heapq.heappush(oper,int(num))
        elif command == 'D':
            if len(oper) == 0:
                continue
            if int(num) == -1:
                heapq.heappop(oper)
            elif int(num) == 1:
                oper.remove(max(oper))
                heapq.heapify(oper)
    if len(oper) == 0 :
        return [0,0]
    else:
        return[max(oper),oper[0]]

operations = ["I 7","I 5","I -5","D -1"]	# return [7,5]
# operations = ["I 16","D 1"]	# return [0,0]

print(solution(operations))
