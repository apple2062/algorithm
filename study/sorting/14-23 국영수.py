# 국영수
# 시간 복잡도: O(N log N)

n = int(input()) # 학생수
matrix = []
for i in range(n):
    name, kor, eng, math = input().split()
    matrix.append((name,int(kor),int(eng),int(math))) # 이름, 국어, 영어, 수학
matrix = sorted(matrix,key = lambda x:(-x[1],x[2],-x[3],x[0]))
for i in matrix:
    print(i[0])
