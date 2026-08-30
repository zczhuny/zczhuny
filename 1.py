# 输入部分
name = input("请输入你的名字：")
age = input("请输入你的年龄：")
height = float(input("请输入你的身高（米）："))

# 计算部分
height_cm = height * 100

# 输出部分
print(f"大家好，我叫{name}，今年{age}岁，身高{height_cm:.5f}厘米！")