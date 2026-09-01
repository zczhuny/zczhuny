def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return None        # 特殊情况：返回"没有结果"
    return a / b           # 正常情况：正常算

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

result1 = add(a, b)
result2 = sub(a, b)
result3 = mul(a, b)
result4 = div(a, b)

print(f"{a} + {b} = {result1}")
print(f"{a} - {b} = {result2}")
print(f"{a} * {b} = {result3}")
if result4 is None:
    print(f"{a} / {b} = 不能除以0！")
else:
    print(f"{a} / {b} = {result4}")