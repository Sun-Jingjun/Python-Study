# 一个最简单的函数例子：斐波那契
def add(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return add(n - 1) + add(n - 2)


for i in range(1, 10):
    print('{}:{}'.format(i, add(i)))
