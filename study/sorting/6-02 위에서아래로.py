# 6-2 위에서 아래로

# 크기에 상관없이 나열되어 있다.
# 큰 숫 부터 작은 수 순서로 정렬 . 내림차순 정렬 프로그램 만들기

n = int(input())
matrix = []
for i in range(n):
     matrix.append(int(input()))
matrix.sort(reverse=True)
for i in matrix:
    print(i,end = ' ')


