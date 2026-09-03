s = [12,23,34,45,56,67,78,89,90]
print(sum(s))
print(f"Average = {sum(s)/len(s):.1f}")
print(f"Max = {max(s)}")
print(f"Min = {min(s)}")
p = 0
for i in range(len(s)):
    if s[i]>=60:
        print(f"{s[i]} is a passing score")
        p = p + 1
print(f"Total passing scores = {p}")
