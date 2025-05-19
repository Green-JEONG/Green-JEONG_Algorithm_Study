scores = []

for _ in range(20):
    scores.append(int(input()))
    
w_scores = sorted(scores[:10], reverse=True)
k_scores = sorted(scores[10:], reverse=True)
    
w_total = sum(w_scores[:3])
k_total = sum(k_scores[:3])

print(w_total, k_total)