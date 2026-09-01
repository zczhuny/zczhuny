def is_even(n):
    return n % 2 == 0
n = int(input("请输入一个整数："))
for i in range(1, n + 1):
    if is_even(i):
        print(i)