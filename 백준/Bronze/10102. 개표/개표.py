v = int(input())
votes = input()

a_count = votes.count("A")
b_count = votes.count("B")

if a_count > b_count:
    print("A")
elif a_count < b_count:
    print("B")
else:
    print("Tie")