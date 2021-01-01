testcase 1.
5
5
1 5
2 3 4
9 4 1 7
6 7 1 9 3 >> 30

testcase 2.
4
16
33 22
63 17 10
10 11 61 57 >> 127

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(0,n)]

for i in range(1,n):
    for j in range(len(matrix[i])):
        if j == 0 :
            matrix[i][j] += (matrix[i-1][j])
        elif j==i:
            matrix[i][j] +=(matrix[i-1][j-1])
        else :
            matrix[i][j] += (max(matrix[i-1][j],matrix[i-1][j-1]))
print(max(matrix[-1]))
