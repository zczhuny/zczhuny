d = {}
t = input()

for i in t:
    if i == " ":
        continue
    d[i] = d.get(i, 0) + 1
for k, v in d.items():
    print(f"{k}:{v}次", end="\t")

bn = ""
bv = -1
if d:
    for k1, v1 in d.items():
        if v1 > bv:
            bv = v1
            bn = k1
    print("\n" + "出现最多次数的字符：")
    for k2, v2 in d.items():
        if v2 == bv:
            print(f"  {k2}", end="")
    print("\n" + f"最大出现次数：{bv}")