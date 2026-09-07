with open("mydialiy.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")
for i in open("mydialiy.txt", "r", encoding="utf-8"):
    i = i.strip()
    print(i)