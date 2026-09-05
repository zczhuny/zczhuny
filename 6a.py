s = {"chinese":70,"maths":80,"english":90}
s["history"] = 100
s["chinese"] = 75
print(s["maths"])
print(len(s))
for a, b in s.items():
    print(f"{a}:{b}")