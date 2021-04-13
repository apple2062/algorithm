def solution(n):
    val = "0"
    for j in range(n):
        new_val = ""
        for i in val:
            if i=="1":
                new_val += "0"
            else:
                new_val += "1"
        val = val+ new_val
    return val[n-1]
