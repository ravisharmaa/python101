class Animal(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('%s is eating %s!' %(self.name, food))

# Inheriting


class Dog(Animal):

    def fetch(self, thing):
        print('%s goes after the %s!' %(self.name, thing))


class Cat(Animal):

    def swat_string(self):
        print('%s shreds the string' %(self.name))


rover = Dog('rover')
jerry = Cat('jerry')

rover.fetch('paper')
rover.eat('soup')
jerry.eat('milk')

jerry.swat_string()


