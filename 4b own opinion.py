
def is_even(n):
    print("1到n之间的奇偶，输入n的值为：", n)
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(f"{i} 是偶数")
        else:
            print(f"{i} 是奇数")
n = int(input())
is_even(n)