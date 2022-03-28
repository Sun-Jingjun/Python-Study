#
# 测试file的read，readline，readlines方法的区别
#

with open('read.txt', 'r', encoding='utf-8') as file:
    line1 = file.read()  # 未指定大小一次性读完，\n不会读
    line2 = file.readline()  # 只读一行，读到\n换行结束，\n也会读入
    line3 = file.readlines()  # 读完所有行，返回一个列表

    line4 = file.read(20)  # 只读4个字节
    line5 = file.readline(4)  # 只读4个字节
    line6 = file.readlines(4)  # 看该字节可以读到多少行，然后把当前位置的行也读完

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
