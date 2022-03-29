# 函数式编程，使用lambda表达式，用来替换匿名函数
# 函数式编程还有一个特点，需要保证函数不可变。比如对一个列表对所有数字乘以2，那这样列表对值就改变了，如果要满足函数式对条件，则需要返回一个新的
# 列表，这样多次调用保证结果相等。？？？todo 这里不是很懂和保证结果相等有什么关联


# 函数式有三个主要使用对方法，
# map(func, iterbale) ：对所有对iterbale执行func，并返回执行后对结果
# filter(func, iterable) : 对所有对iterable执行func，返回结果为ture的列表
# reduce(func,iterable) : 对所有的iterable执行func，func有两个参数，x，y，其中一个为当前迭代，一个为上次迭代的结果。但是测试过程中发现被删除了在py3




def test_map():
    list = [1, 2, 3, 4, 5]
    new_list = map(lambda x: x+1, list)
    for v in new_list:
        print(v)


def test_filter():
    list = [1, 2, 3, 4, 5]
    new_list = filter(lambda x: x>1, list)
    for v in new_list:
        print(v)
