#프로그래머스 (삼각 달팽이)
#삼각형이라고 무조건 삼각형 형태로 만들겠단 내 생각이 문제였음..사각형으로 선언 후에, 0인 요소를 없애주는 faltten을 활용한다던지(chain에 대해 알아볼것),
#0을 제외한 놈들로만 새 배열에 담는 생각을 안했다.. matrix를 사각형으로 선언했어야 했구나..

def solution(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    answer = [] # 최종으로 matrix에서 0인 놈 빼고 담을 배열
    x,y = -1,0 #화살표 순서가 하-우-상 이기 때문에 맨 처음 하 시작할때 (0,0) 으로 만들기 위해 x가 -1부터 시작
    value = 1

    for i in range(n): #n과 화살표를 수행하는 횟수가 동일하기 떄문에 횟수를 세주기 위함
        for j in range(i,n): #화살표에 따라 채워지는 칸 수가 n->(n-1)->(n-2)->...->1 이라 채울 칸 수 선언해주기 위함
            #down
            if i%3 == 0:
                x += 1
            #right
            elif i%3 == 1:
                y += 1
            #up
            elif i%3 == 2:
                x -= 1
                y -= 1

            matrix[x][y] = value
            value+=1
    for i in matrix:
        for j in i:
            if j!=0:
                answer.append(j)
    return answer

n = int(input())
print(solution(n))
