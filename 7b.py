s = {}
n = ""
s_re = ""
while True:
    n = input("输入姓名（q 退出）：")
    if  n == "q":
        break
    s[n] = float(input("输入分数："))

with open("score.txt","a", encoding="utf-8") as f:
    for k,v in s.items():
        f.write(f"{k}:{v}\n")

with open("score.txt","r", encoding="utf-8") as f:
    for l in f:
        n, s_re = l.strip().split(":")
        s[n]= float(s_re)

for k2,v2 in s.items():
    print(f"{k2}:{v2}分")

bn = ""
bs = -1
if s_re:
    for k3,v3 in s.items():
        if v3 > bs:
            bs = v3
            bn = k3

    print(f"最高分：{bs}分")
    print(f"拿到最高分的人：")
    for k4,v4 in s.items():
        if v4 == bs:
            print(f"{k4}", end=" ")