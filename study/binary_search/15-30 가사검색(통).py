v=# 가사 검색

# 첫 번째 풀이 ( 시간 복잡도 : O(N log N) + O(M * logN) ..? )
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
        reverse_candidate[len(word)].append(word[-1::-1])

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


-----------------------------------------------------------------------------------------------------
# 두번째 풀이 (trie 자료구조)

import sys
from bisect import bisect_left, bisect_right


class Node(object):
    def __init__(self, key):
        self.key = key  # 시작 값( 바로 이전의 값)
        self.remain_length = {}  # 터미널까지 남아있는 문자열의 길이 ex) {3:1, 2:3...} : 남은 노드 길이가 3인게 1개, 길이가 2인게 3개...
        self.children = {}  # 자식


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # key 에는 문자, length에는 남아있는 string 의 길이를 담았음
    def insert(self, string):
        curr_node = self.head

        remain_length = len(string)  # 처음 string의 전체 길이
        if remain_length in curr_node.remain_length:
            curr_node.remain_length[remain_length] += 1
        else:
            curr_node.remain_length[remain_length] = 1

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]
            remain_length -= 1
            if remain_length in curr_node.remain_length:
                curr_node.remain_length[remain_length] += 1
            else:
                curr_node.remain_length[remain_length] = 1

    def search_count(self,string,check_length): # string: 물음표가 아닌 놈들의 char들 / check_length = 물음표의 개수
        curr_node = self.head
        # 찾아야할 ?를 포함한 string의 길이가 없다면 return 0
        if check_length + len(string) not in curr_node.remain_length:
            return 0

        for char in string:
            # 찾아야할 string 이 없다면 return 0
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return 0

        # string 은 존재하는데 check_length 가 remain_length 에 있는지 확인
        if check_length in curr_node.remain_length:
            return curr_node.remain_length[check_length]
        else:
            return 0

def solution(words, queries):
    t = Trie()
    inv_t = Trie()
    for word in words:
        t.insert(word)
        inv_t.insert(word[-1::-1])

    answer = []
    for i in range(len(queries)):
        query = queries[i]
        if query[0] is '?':  # 시작이 '?'
            query = query[-1::-1]
            chars = query.replace("?", "")
            check_length = len(query)-len(chars)
            # end = query.find('?')
            # chars = query[:end]
            answer.append(inv_t.search_count(chars, check_length))
        else: # 시작이 알파벳
            chars = query.replace("?", "")
            check_length = len(query) - len(chars)
            # end = query.find('?')
            # chars = query[:end]
            answer.append(t.search_count(chars, check_length))

    return answer

