# 줄 세우기 (https://www.acmicpc.net/problem/2631)
'''
처음 생각한 아이디어 : 맨 처음 주어진 배열에 대해서 LIS 를 구한 뒤에 , 그 원소 값을 제외한 나머지 친구들은 자리를 바꿔주어야 함.
                >> (전체 배열의 길이) - (LIS) 길이를 빼주면 될 듯..?

근데 위 아이디어 생각하기까지 진짜 엄청 시간 오래 걸렸고, 처으멩 진짜 온갖 정렬 알고리즘 가지고 가장 최소 횟수 구해볼까 뻘 생각도 했음..
'''
#  선생님은 1번부터 N번까지 번호가 적혀있는 번호표를 아이들의 가슴에 붙여주었다.
#  위치를 옮기는 아이들의 수를 최소로
#  N명의 아이들이 임의의 순서로 줄을 서 있을 때, 번호 순서대로 배치하기 위해 옮겨지는 아이의 최소 수를 구하는 프로그램

from bisect import bisect_left

def lis(children):
    stack = [0]
    for i in children:
        if stack[-1] < i:
            stack.append(i)
        else:
            stack[bisect_left(stack,i)] = i
    return len(stack) - 1

n = int(input()) # 아이의 수
children = []
for _ in range(n):
    children.append(int(input()))
    
print(n-lis(children))

