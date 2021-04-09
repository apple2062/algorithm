# 큰 수 만들기 ( https://eda-ai-lab.tistory.com/465 ) <<< ref link


def solution(number, k):
    storage = [number[0]]
    for i in number[1:]:
        # storage 에 들어오는 i값이 storage[-1]보다 크다면, 기존 값 제거하고 그 뒤에 붙여주는 작업
        while len(storage) > 0 and storage[-1] < i and k>0:
            storage.pop()
            k-=1
        storage.append(i)
    # 전부 제거된 게 아니라면, 남은 부분은 단순히 slicing ( 그 예 : 987654321 , k=3 이면 return 987654321 인 상태)
    if k!=0:
        storage = storage[:-k]
    return ''.join(storage)
   
