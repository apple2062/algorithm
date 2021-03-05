# 메뉴 리뉴얼 (https://programmers.co.kr/learn/courses/30/lessons/72411)
'''
첫번째 풀이 : defaultdict()
두번째 풀이 : Counter() 

이런 유형 둘 중 뭐 쓰는게 더 나은지
'''

# sol 1
'''
시간 복잡도가 O(n^4) 이 넘어가는데(3중 for), 시간 더 줄일 수 있는 방법 추천받아보기
처음 접근 방식 : 각 코스 구성 원소에 따른 COmbinations 조합들에 대한 개수를 저장하기 위해, defaultdict() 를 활용하고자 함
                1. orders에 대한 쓰인 원소들 집합 alpa set 초기 선언
어려웠던 부분 : defaultdict() 까지 만드든 건 어려움이 없었지만, 생성한 dict 에서 value 값의 max 가 두개 이상 존재 하는 경우,
            아이디어 생각하느라 고생했다..ㅋㅋ max value 가 두 개 이상이었던 경우 처리가 어려웠음
            +
            course 보다 max_alphlen 의 길이가 짧은 경우, course 배열을 변경해주어야 하는데 그걸 처음에 안해서 틀렸었다.
'''

from collections import defaultdict
from itertools import combinations

def menu_combo(alpha, i):
    menu = defaultdict(int)
    for i in combinations(alpha, i):
        menu[i]
    return menu

def solution(orders, course):
    answer = []
    alpha = set()
    max_alphlen = 0
    idx = 0
    for i in orders:
        max_alphlen = max(max_alphlen, len(i))
        for j in i:
            alpha.add(j)
        orders[idx] = ''.join(sorted(i))
        idx+=1
    alpha = sorted(list(alpha))
    course = [i for i in course if i<=max_alphlen]
    for i in course:  # course 에 주어 단품 메뉴 개수 마다
        possible_menu = menu_combo(alpha, i) # 가능한 메뉴 조합의 수
        for j in orders:
            menu = combinations(j, i)
            for k in menu:
                possible_menu[k] += 1
        key_max = max(possible_menu.items(), key=lambda x: x[1])  #value 값이 최대인 (key , value) 쌍 리턴진
        # 사람들이 두 명 이상 추천했다면
        if key_max[1] >= 2:
            for k,l in possible_menu.items():
                if l == key_max[1]:
                    answer.append(''.join(list(k)))
    return sorted(answer)









---------------------------------------------------------------------------------------------

# sol 2

from collections import Counter
from itertools import combinations

def solution(orders,course):
    answer = []
    for i in course:
        possible_menu =[]
        for j in orders:
            for k in combinations(sorted(j),i):
                possible_menu.append(''.join(k))
        max_menu = Counter(possible_menu).most_common() #value 가 높은 순으로 dict 나열
        max_value = max_menu[0][1]
        for l in max_menu:
            if l[1] == max_value and [1]>=2:
                answer.append(l[0])
    return sorted(answer)

