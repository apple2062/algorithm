from itertools import *

def solution(numbers):
    answer = []
    for i in permutations(numbers,2):
        if i[0] + i[1] not in answer:
            answer.append(i[0] + i[1])
    return sorted(answer)
