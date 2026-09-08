d = {}
t = ""
with open("mydiary.txt","r",encoding="utf-8") as f:
    for l in f:
        t = l.strip("\n")
        for c in t:
            d[c] = d.get(c,0) + 1

bt = -1
if d:
    for k,v in d.items():
        if v > bt:
            bt = v
    
    print(f"最大出现次数：{bt}")
    print(f"出现最多次数的字符有：")
    for k1,v1 in d.items():
        if v1 == bt:
            print(f"{k1}",end="  ")