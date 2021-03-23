# 탑 ( https://www.acmicpc.net/problem/2493 )


def solution(matrix):
    answer = []
    matrix.reverse()
    for i in range(n-1):
        for j in range(i+1,n):
            if matrix[i]<matrix[j]:
                #print(i,matrix[i],matrix[j])
                answer.append(5-matrix.index(matrix[j]))
                break
            if j == (n-1):
                answer.append(0)
    answer.append(0) #이 부분 다시 작업하고 난뒤에 answer 다시 reverse 해주기
    return answer


n = int(input()) #탑의 수
matrix = list(map(int,input().split()))
print(solution(matrix))

-------------------------------------------------------------

# 탑 ( https://www.acmicpc.net/problem/2493 )

n = int(input())
matrix = list(map(int,input().split()))
stack = []
answer = [0] * n

for i in range(n):
    target = matrix[i]
    while stack and matrix[stack[-1]] < target :
        stack.pop()
    if stack:
        answer[i] = stack[-1] + 1
    stack.append(i)

print(' '.join(list(map(str, answer))))


