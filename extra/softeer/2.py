'''
로봇들의 위치에서 거리가 K 이하인 부품만 잡을 수 있다.왼쪽 오른쪽은 상관 없다.
라인의 길이 N, 부품을 집을 수 있는 거리 K, 그리고 로봇과 부품의 위치가 주어졌을 때 부품을 집을 수 있는 로봇의 최대 수를 구하는 프로그램을 작성

부품을 집을 수 있는 최대 로봇 수 출력
'''
from collections import deque
def solution(n,k,line):
    answer = 0
    robot = [i for i in range(len(line)) if line[i]=='P']
    machine = deque([i for i in range(len(line)) if line[i]=='H'])
    print(robot,machine)

    while machine:
        val = machine.popleft()
        for i in range(1,k+1):
            if val-i in robot:
                robot.remove(val-i)
                print(robot)
                answer+=1
                continue
            elif val+i in robot:
                robot.remove(val+i)
                print(robot)
                answer+=1
                continue
    return answer



n,k = map(int,input().split()) # 라인의 길이, 부품을 잡을 수 있는 거리
line = list(input()) # 문자 P(로봇) /  H(부품) 

print(solution(n,k,line))
'''
20 1
HHPHPPHHPPHPPPHPHPHP
>>> return 8

12 1
HPHPHPHHPPHP
>>> return 5

12 2
HPHPHPHHPPHP
>>> return 6

'''
