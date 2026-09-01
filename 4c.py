def bmi(weight1, height1):
    return weight1 / height1 ** 2

weight = float(input("请输入体重（kg）："))
height = float(input("请输入身高（m）："))

print(f"您的BMI值为：{bmi(weight, height):.2f}")