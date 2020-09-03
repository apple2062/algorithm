def solution(length,weight,truck):
    sec = 0
    bridge = [0]*length 
    while truck:
        bridge.pop(0)
        sec+=1
        if sum(bridge)+truck[0] <= weight:
            bridge.append(truck.pop(0))
        else:
            bridge.append(0)
    return sec+len(bridge)

