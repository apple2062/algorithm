# 가사 검색
'''
Trie 자료구조 활용
'''

# 각 키워드 별로 매치된 단어가 몇 개인지 순서대로 반환
# 검색 키워드는 중복될 수도 있습니다.
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
