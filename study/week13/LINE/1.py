def solution(table, languages, preference):
    answer = ''
    matrix = []
    for i in table:
        matrix.append(i.split())
    sum_set = [0 for _ in range(len(table))] #[SI,CON,HARD,POR,GAME]
    for i in range(len(languages)):
        for j in range(len(matrix)):
                if languages[i] in matrix[j]:
                    sum_set[j] += (5-matrix[j].index(languages[i])+1)*preference[i]

    max_ = max(sum_set)
    print(sum_set)
    value = []
    for i in range(len(sum_set)):
        if sum_set[i] == max_:
            value.append(matrix[i][0])
    value.sort()
    answer += value[0]
    return answer

