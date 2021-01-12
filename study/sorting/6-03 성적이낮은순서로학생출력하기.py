# 6-3 성적이 낮은 순서로 학생 출력하기

n = int(input())
matrix = []
for i in range(n):
    name,score = map(str,input().split())
    matrix.append((name,int(score)))
matrix = sorted(matrix,key = lambda x:x[1])
for i in matrix:
    print(i[0], end = ' ')


