n = int(input())
grades = list(map(int, input().split()))

m = max(grades)
new_grades = []

for i in grades:
    i = i / m * 100
    new_grades.append(i)
    
print(f"{sum(new_grades) / n:.2f}")