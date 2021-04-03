def solution(enroll, referral, seller, amount):
    answer = [0 for x in range(len(enroll))] 
    
    enrollDict= {}
    for i in range(len(enroll)):
        enrollDict[enroll[i]] = {"idx" : i, "ref": referral[i] }
        
            
    for i in range(len(seller)) :
        sellPerson = seller[i]
        sellAmount = amount[i] * 100
        refMoney = int(sellAmount / 10)
        answer[enrollDict[sellPerson]["idx"]] += sellAmount - refMoney
        nextRef = enrollDict[sellPerson]["ref"]
        while (nextRef != "-" and refMoney > 0):
            sellPerson = nextRef
            sellAmount = refMoney
            refMoney = int(sellAmount / 10)
            answer[enrollDict[sellPerson]["idx"]] += sellAmount - refMoney
            nextRef = enrollDict[sellPerson]["ref"]
        
    return answer
