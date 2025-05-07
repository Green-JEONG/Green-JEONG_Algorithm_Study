present = list(map(int, input().split(":")))
start = list(map(int, input().split(":")))

present_sec = present[0] * 3600 + present[1] * 60 + present[2]
start_sec = start[0] * 3600 + start[1] * 60 + start[2]
                                     
if start_sec < present_sec:    # 임무 시작 시간: 실제로 범인을 잡기로 정해진 시각 (끝 시점)
    start_sec += 24 * 3600
    
remain = start_sec - present_sec

h = remain // 3600
m = (remain % 3600) // 60
s = remain % 60

print(f"{h:02d}:{m:02d}:{s:02d}")