class Person():
    def __init__(self, name, age, id_card):
        print('person init')
        self.name = name
        self.age = age
        self.id_card = id_card

    def __str__(self):
        return 'person : {} , age : {}'.format(self.name, self.age)

    def get_name(self):
        return self.name


class Student(Person):
    def __init__(self, name, age, id_card, grade, remark):
        Person.__init__(self, name, age, id_card)
        self.grade = grade
        self.remark = remark

    def get_remark_len(self):
        return len(self.remark)

    def get_name(self):
        return 'stu:{}'.format(self.name)


stu = Student('sun', '23', '11111', '98', 'test')
print(stu)
# 直接访问父类的变量和方法
print('stu.name:{}'.format(stu.age))
# 方法重写
print(stu.get_name())

