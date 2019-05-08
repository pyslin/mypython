class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')
#class 是一种数据类型 和list str一样的
dog = Dog()
dog.run()
cat =Cat()
cat.run()

a = list()
b = Animal()
c = Dog()
print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Animal))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
#新增一个Animal的子类,不必对run_twice()做任何修改
#任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
#对扩展开放：允许新增Animal子类；
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
#我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly..')


run_twice(Tortoise())
