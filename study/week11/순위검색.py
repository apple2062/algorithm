def solution(info, query):
    answer = []
    for q in query:
        cnt = 0
        query_ = q.split()
        #print(query_)
        for i in info:
            i = i.split()
            if query_[0] != '-':
                if query_[0] != i[0]:
                    continue
            if query_[2] != '-':
                if query_[2] != i[1]:
                    continue
            if query_[4] != '-':
                if query_[4] != i[2]:
                    continue
            if query_[6] != '-':
                if query_[6] != i[3]:
                    continue
            if int(query_[7]) <= int(i[4]):
                cnt += 1
        answer.append(cnt)
    return answer
