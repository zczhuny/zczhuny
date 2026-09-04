score = {}
name = ""

while True:
    name = input("输入姓名（q 退出）：")
    if name == "q":
        break
    
    s = float(input(f"{name} 的成绩："))
    score[name] = s
if score:
    print("全班成绩：")
for k1, v1 in score.items():
    print(f"{k1}: {v1}")

best_name = ""
best_score = -1
if score:
    for k2, v2 in score.items():
        if v2 > best_score:
            best_score = v2
            best_name = k2
    print(f"最高分：{best_score}分")
    print("拿到最高分的人：")
    for k3, v3 in score.items():
        if v3 == best_score:
            print(f"  {k3}")
else:
    print("没有输入！")

#if best_name == "":
#    print("没有输入！")
#else:
#    print(f"最高分：{best_name}，{best_score}分")