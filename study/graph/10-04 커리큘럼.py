# 커리큘럼 (10-04)
'''
선수 강의 -> 위상정렬 문제
'''
from collections import deque
import sys
import copy # class_time 리스트를 복사하기 위함
input = sys.stdin.readline

def topology_sort():
    q = deque()
    answer = copy.copy(class_time)
    print("answer",answer)
    for i in range(1,n+1):
        if in_line[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()
        for i in classes[node]:
            in_line[i] -= 1
            answer[i] = max(answer[i],class_time[i] + answer[node])
            print(answer)
            if in_line[i] == 0:
                q.append(i)

    # 정렬 끝난 뒤 출력
    for i in answer[1:]:
        print(i)

n = int(input()) #강의의 수
# 진입차수 초기화
in_line = [0] * (n+1)
classes = [[] for _ in range(n+1)]
class_time = [0] * (n+1)

for k in range(1,n+1):
    lst = list(map(int,(input().split()))) # 강의 시간, 선수 과목들의 번호, -1로 line 종료
    class_time[k] = lst[0] #강의 시간 저장
    for i in lst[1:-1]:
        classes[k].append(i)
        in_line[k] += 1
print(classes,in_line)

topology_sort()




