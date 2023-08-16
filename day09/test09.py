class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def run(self):
        print(f'{self.name}在以{self.speed}的速度在跑')

    @classmethod
    def class_method(cls):
        print('class method')


car = Car('宝马', 366)
car.age = 90
print(car.age)
car.run()
Car.run(car)
Car.class_method()

class Animal:
    def __init__(self):
        print('我是构造函数' + self.__class__.__name__)


Animal()
