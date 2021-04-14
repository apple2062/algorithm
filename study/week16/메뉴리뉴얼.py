from collections import Counter
from itertools import combinations

def solution(orders,course):
    answer = []
    for i in course:
        possible_menu =[]
        for j in orders:
            for k in combinations(sorted(j),i):
                possible_menu.append(''.join(k))
        max_menu = Counter(possible_menu).most_common()
        max_value = max_menu[0][1]
        for l in max_menu:
            if l[1] == max_value and l[1]>=2:
                answer.append(l[0])
    return sorted(answer)
