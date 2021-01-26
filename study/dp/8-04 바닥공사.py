# 바닥 공사
'''
처음에는 이게 왜 dp 인가 싶었는데 생각해보니
길이가 i 부터 시작해서 점점 늘어난다 하면,
i+2 는 무조건 (2X2) 1개나 , (2X1) 2개가 붙는것이고 i+1은 무조건 (2X1) 1개 뿐이기 떄문에
해당 경우에 대해서만 고려해 주면 된다.
'''
# 가로 N, 세로 2
def solution(n):
    tile = [0]*1001 # 타일 개수에 대한 dp 선언
    tile[1] = 1 # (1X2)
    tile[2] = 3 # (2X1)*2 OR (2X2) AND (1X2)*2
    for i in range(3,n+1):
        tile[i] = (tile[i-1] + tile[i-2]*2) % 796796
    return tile[n]

n = int(input()) #3 >> return 5
print(solution(n))
