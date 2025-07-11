def solution(keyinput, board):
    x, y = 0, 0
    
    x_limit = board[0] // 2 # 가로 최대 절반
    y_limit = board[1] // 2 # 세로 최대 절반
    
    for key in keyinput:
        if key == "left":
            if x > -x_limit:
                x -= 1
        elif key == "right":
            if x < x_limit:
                x += 1
        elif key == "up":
            if y < y_limit:
                y += 1
        else:
            if y > -y_limit:
                y -= 1
                
    return [x, y]