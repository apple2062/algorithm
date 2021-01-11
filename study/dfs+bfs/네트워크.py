# 네트워크

def solution(n,computers):
    answer = 0 #네트워크 개수
    visited = [0 for _ in range(n)]

    def dfs(start):
        point = [start]

        while point:
            computer = point.pop()
            if visited[computer] == 0:
                visited[computer]   = 1
            for i in range(len(computers[0])):
                if computers[computer][i] == 1 and visited[i] == 0:
                    point.append(i)

    i = 0
    while True:
        if 0 not in visited:
            break
        if visited[i] == 0:
            dfs(i)
            answer += 1
        i += 1
    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

