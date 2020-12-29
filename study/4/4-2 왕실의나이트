# 왕실의 나이트(O(n))

# 8*8 좌표 평면 , 나이트는 L자 형태로 이동 가능
# 수평으로 두 칸 이동뒤 수직으로 한 칸
# 수직으로 두칸 이동 뒤 수평으로 한 칸

# 나이트가 이동할 수 있는 경우의 수 출력

def solution(s):
    answer = 0
    # print(ord(a)) == 97, 체스 판의 맨왼쪽 위가 (1,1) 므로 int(s[1]) -1 
    x,y = ord(s[0])-97 , int(s[1])-1
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<8 and 0<=ny<8:
            answer+=1
    return answer

# 갈 수 있는 좌표의 전체 경우의 수
dx = [-1,1,2,2,-2,-2,-1,1]
dy = [2,2,-1,1,1,-1,-2,-2]

s = list(input())
print(solution(s))
