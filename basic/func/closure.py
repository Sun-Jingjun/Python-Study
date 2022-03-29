# 完成一个闭包的例子，使用函数封装幂运算的次方，后续只用传入基础即可

def pow(n):
    def pow_cal(base):
        return base ** n

    return pow_cal


n2 = pow(2)
n3 = pow(3)

print(n2(2))
print(n3(2))
