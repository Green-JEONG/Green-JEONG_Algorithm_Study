def solution(X, Y):
    cntX = [0] * 10
    cntY = [0] * 10

    for ch in X:
        cntX[int(ch)] += 1

    for ch in Y:
        cntY[int(ch)] += 1

    result = []

    for num in range(9, -1, -1):
        use = min(cntX[num], cntY[num])
        result.append(str(num) * use)

    answer = ''.join(result)

    if answer == "":
        return "-1"

    if answer[0] == "0":
        return "0"

    return answer
