#06 무지의 먹방 라이브 (프로그래머스 42891 level4)

def solution(food,k):
    idx = 0
    #print(food)
    while True:
        # 더이상 섭취할 음식이 없을 때
        if sum(food) == 0:
            return -1
        # 네트워크 장애 발생 시
        if k == 0:
            if food[idx] == 0:
                while True:
                    if food[idx] !=0:
                        break
                    idx = (idx +1) % len(food)
            return idx+1
        # 음식을 다 먹은 경우
        if food[idx] == 0 :
            while True:
                if food[idx] != 0:
                    break
                idx = (idx + 1) % len(food)
        food[idx] -= 1
        idx = (idx+1) % len(food)
        #print("target:", idx, food)
        k -= 1

#food_times=[4,2,3,6,7,1,5,8]
#k=16 #answer = 3

food_times=[4,2,3,6,7,1,5,8]
k=27 #answer = 5
print(solution(food_times,k))
