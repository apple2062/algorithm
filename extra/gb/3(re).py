import heapq as hq

def solution(N, coffee_times):
    # 1 일때 예외 처리
    if N == 1:
        return [x for x in range(1, len(coffee_times) + 1)]
    answer = []
    coffee_dict = []
    q = []

    for i in range(len(coffee_times)):
        coffee_dict.append([coffee_times[i], i+1]) #(value, id)
    for i in range(N):
        q.append(coffee_dict.pop(0))
    hq.heapify(q)

    while q:
        info = q.pop(0)
        answer.append(info[1])
        for i in range(len(q)):
            q[i][0] -= info[0]
        if len(coffee_dict) > 0:
            hq.heappush(q,coffee_dict.pop(0))
        hq.heapify(q)
    return answer

N , coffee_times  = 3, [4,2,2,5,3] # return [2, 3, 1, 5, 4]
print(solution(N,coffee_times))
