with open("mydiary.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")
with open("mydiary.txt", "r", encoding="utf-8") as f:
    for i in f:
        print(i.strip())