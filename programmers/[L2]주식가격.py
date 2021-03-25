def solution(prices): #[1,2,3,2,3]
    ans = []
    for i in range(len(prices)-1):
        sec = 0
        for j in range(i+1,len(prices)):
            sec+=1
            if prices[j] < prices[i]:
                break
        ans.append(sec)
    ans.append(0)

