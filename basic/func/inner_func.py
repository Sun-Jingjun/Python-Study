# 内部函数，函数内部可以嵌套定义函数，内部定义的函数不会被外部调用,当然这里的前提是有内部定义函数的必要性：
# 1.在内部会重复调用  2.返回配置密码等函数不想给外部调用，但是还想保证封装等特性
# 完成一个阶乘的例子

def factorial(n):
    def inner_factor(n):
        if n <= 1:
            return 1
        return n * inner_factor(n - 1)

    if not isinstance(n, int):
        raise Exception('input is not a num')
    if n <= 0:
        return 0
    return inner_factor(n)


print(factorial(-1))
