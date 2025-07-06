n = int(input())

book_counts = {}

for _ in range(n):
    title = input()
    if title in book_counts:
        book_counts[title] += 1
    else:
        book_counts[title] = 1
        
max_count = max(book_counts.values())

best_sellers = []
for title in book_counts:
    if book_counts[title] == max_count:
        best_sellers.append(title)
        
print(min(best_sellers))