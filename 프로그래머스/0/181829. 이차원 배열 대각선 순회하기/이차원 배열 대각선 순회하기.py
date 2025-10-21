def solution(board, k):
    total = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i + j <= k:
                total += board[i][j]
                
    return total