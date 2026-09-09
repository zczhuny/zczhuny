import random

secret = random.randint(1, 100)   # 抽答案：1~100 里的一个整数
count = 0                          # 计数器：猜了几次

# print(secret)  # ← 调试用，测试完删掉这行！

while True:                        # 一直猜，直到猜中
    guess = int(input("猜一个 1~100 的数："))   # 玩家输入，字符串转整数
    count += 1                     # 每猜一次 +1（猜中那次也要算）

    if guess > secret:             # 猜大了
        print("猜大了，再小一点")
    elif guess < secret:           # 猜小了
        print("猜小了，再大一点")
    else:                          # 不大不小 = 猜中了
        print(f"恭喜猜中！一共猜了 {count} 次")
        break                      # 猜中了，跳出 while，游戏结束