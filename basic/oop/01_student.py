# 通过一个Student来学习oop
class Student():
    def __init__(self, name, age, famous_remark):
        print('init ...')
        self.__name = name
        self.age = age
        self.famous_remark = famous_remark

    def set_remark(self, remark):
        self.famous_remark = remark

    # 相当与tostring方法
    def __str__(self):
        return 'student:{} ,the age is {},the remark: {}'.format(self.__name, self.age, self.famous_remark)


stu1 = Student('sun', 19, 'To be both a speaker of words and a doer of deeds.')
stu2 = Student('li', 21, ' ')
stu2.famous_remark = 'There is no royal road to learning.'

print(stu1)
print(stu2)

# 加上__后，name为私有属性，无法访问
# print(stu1.name)
