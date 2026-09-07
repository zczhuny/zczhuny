d = {}
t = ""
with open("mydialiy.txt","r",encoding="utf-8") as f:
    for l in f:
        t = l.strip()
        for c in t:
            d[c] = d.get(c,0) + 1

bt = -1
bn  = ""
if d:
    for k,v in d.items():
        if v > bt:
            bt = v
            bn = k
    
    print(f"最大出现次数：{bt}")
    print(f"出现最多次数的字节有：")
    for k1,v1 in d.items():
        if v1 == bt:
            print(f"{k1}",end="  ")