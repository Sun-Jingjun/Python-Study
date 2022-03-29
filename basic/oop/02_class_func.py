# 类函数，静态函数，成员函数
# 还是通过Student的例子来进行讲解
class Student():
    SCHOOL = 'xatu'

    def __init__(self, name, age, famous_remark):
        print('init ...')
        self.__name = name
        self.age = age
        self.famous_remark = famous_remark

    # 类函数,相当于不同的构造函数
    @classmethod
    def create_student_no_remark(cls, name, age):
        return cls(name=name, age=age, famous_remark='no remark')

    # 成员方法，也就是普通方法
    def set_remark(self, remark):
        self.famous_remark = remark

    # 静态方法，不改变动态
    @staticmethod
    def get_all_school():
        return Student.SCHOOL;

    # 相当与tostring方法
    def __str__(self):
        return 'student:{} ,the age is {},the remark: {}'.format(self.__name, self.age, self.famous_remark)


stu1 = Student.create_student_no_remark('sun', 19)
print(stu1)

# 静态方法可以根据类名来调用，也可以通过实例化后的对象的调用
print(Student.get_all_school())
print(stu1.get_all_school())
