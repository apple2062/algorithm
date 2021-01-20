# 가사 검색
from collections import defaultdict
from bisect import bisect_left,bisect_right

def solution(words,queries):
    answer = []
    candidate = defaultdict(list)

    # '**abc' 라면 'cba**' 로 문자열을 뒤집어 주어 *이 접미사가 되도록 바꿔 모든 문자열이 *로 끝나도록 바꿔주기 위함
    reverse_candidate = defaultdict(list)

    # 길이별로 저장
    for word in words:
        candidate[len(word)].append(word)
        #print(candidate)
        reverse_candidate[len(word)].append(word[-1::-1])
        #print(reverse_candidate)

    #정렬
    for cand in candidate.values():
        cand.sort()
    for re_cand in reverse_candidate.values():
        re_cand.sort()

    #탐색
    ''' 탐색법 : queries 중 특정 query 가 'abc**' 라면 start , end = abcaa, abczz 로 정하여 
                그 범위 내의 word 개수를 카운트 해준다. (by using bisect) '''
    for query in queries:
        # 단어가 아닌 ? 로 시작하는 쿼리라면 문자열 reverse 해주어 접근해야 함
        if query[0] == '?':
            target = reverse_candidate[len(query)]
            start,end = query[-1::-1].replace('?','a'), query[-1::-1].replace('?','z') # abc?? -> (aacba,zzcba)
            answer.append(bisect_right(target, end) - bisect_left(target, start))

        # ? 로 시작하는 쿼리라면 그대로 진행
        else:
            target = candidate[len(query)]
            start,end = query.replace('?','a'),query.replace('?','z')
            answer.append(bisect_right(target, end) - bisect_left(target, start))
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words,queries))
