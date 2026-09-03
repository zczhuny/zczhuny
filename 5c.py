hm = []
while True:
    a = float(input("请输入一个身高(输入0结束):"))
    if a == 0:
        break
    else:
        hm.append(a)
if hm:
    print(f"已记录{len(hm)}个人的身高")
    print(f"{max(hm)}是最高的身高")
    print(f"{min(hm)}是最矮的身高")
    print(f"{sum(hm)/len(hm):.1f}是平均身高")
else:
    print("没有记录任何身高")