# 위장 (https://programmers.co.kr/learn/courses/30/lessons/42578#qna )
# 테케 1이 계~~~속 시간초과 났다 ... ㅜㅜㅜㅜㅜ
# 아마 모든 옷의 종류가 하나씩 있는 경우인 것같다. 그럴때 전체 경우의 수는 (2**n)-1 이라서 시간초과 난 것 같다..

def solution(clothes):
    from collections import defaultdict
    from itertools import combinations
    answer = 0
    cloth_type = defaultdict(list)
    for i in clothes:
        cloth_type[i[1]].append(i[0])
        
    for i in range(1,len(cloth_type)+1):
        for j in combinations(cloth_type,i):
            combi = 1
            for k in range(len(list(j))):
                combi *= len(cloth_type[list(j)[k]])
                #print(cloth_type[list(j)[k]])
            answer += combi
    return answer
