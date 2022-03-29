# 全局变量是当前文件所有函数共享的，函数内部不能随意改变全局变量的值

MIN_NUM = 0


# 直接会报编译错误
# def change_num():
#     MIN_NUM = MIN_NUM+1

# 如果想要修改全局变量，需要加上global
def change_num():
    global MIN_NUM
    MIN_NUM = MIN_NUM + 1
    print(MIN_NUM)


change_num()


# 局部变量和全局变量同名，和其他语言相同，以局部变量域为准
def local_var():
    MIN_NUM = 111
    MIN_NUM = MIN_NUM + 1
    print(MIN_NUM)


local_var()
