# 개미 ( https://www.acmicpc.net/problem/2136  )
'''
맞닿으면 방향을 바꾼다는 아이디어때문에 조금 까다롭다고 느껴졌다.
근데 풀이를 참조하니, 개미가 맞닿는 상황은 고려할 필요가 없다는데 그 이유를 아직도 잘 모르겠음..
'''

# 0인 위치나 L인 위치에 도달하게 되면, 그 개미는 막대기 아래로 떨어지게 된다.
# 개미들의 초기상태가 주어졌을 때, 가장 마지막에 떨어지는 개미와 그 개미가 떨어지는 시각을 알아내는 프로그램을 작성하시오.
import sys

n,l = map(int,input().split()) # 개미의 개수, 막대기의 길이
place = []
max_val = -sys.maxsize
min_val = sys.maxsize
for i in range(n):
    number = int(input())
    min_,max_ = min(abs(number), l-abs(number)), max(abs(number), l-abs(number))
    print(min_,max_)
    max_val = max(max_val, max_)
    min_val = min(min_val, min_)
    print(min_val,max_val)
    #place.append(int(input())) # 개미의 위치 ( 양수: 오른쪽 움직 / 음수 : 왼쪽 움직 )
print(max_val,min_val)



