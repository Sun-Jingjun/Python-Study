from abc import abstractmethod, ABCMeta


class Animal(metaclass=ABCMeta):
    # pass是占位符
    @abstractmethod
    def get_type_name(self):
        pass


class Bird(Animal):

    def get_type_name(self):
        return 'bird'


# 抽象类不可以实例化
# a = Animal()
b = Bird()
print(b.get_type_name())
