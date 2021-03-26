
# 치킨 배달

# 도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다.
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리, 도시의 치킨 거리는 모든 집의 치킨 거리의 합
# 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|
# 0은 빈 칸, 1은 집, 2는 치킨집
# 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다. 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성

from itertools import combinations

# 치킨 거리 계산
def solution(chicken_list):
    distance_sum = 0
    # 집집 마다 치킨가게를 전부 돌며 최소거리인 값을 집어 넣음
    for i in house:
        result = 100 ** 100
        for j in chicken_list:
            # 치킨 거리를 돌며 최솟값을 계산합
                result = min(result,abs(i[0]-j[0])+abs(i[1]-j[1]))
        distance_sum += result
    # 치킨 거리의 합
    return distance_sum

n,m = map(int,input().split()) # 도시의 크기, 수익 낼 치킨집의 개수
matrix = list(list(map(int,input().split())) for _ in range(n))
chicken = []
house = []

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 2:
            chicken.append((i,j))
        if matrix[i][j] == 1:
            house.append((i,j))

# 치킨집에서 m 개 선택하여 저장한 리스트
chicken_list = list(combinations(chicken,m))

answer = 100*100
for i in chicken_list:
    distance = solution(i)
    if answer > distance:
        answer = distance
print(answer)
