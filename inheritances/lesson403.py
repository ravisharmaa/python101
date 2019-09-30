class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(self.name + ' le ' + food + ' khancha')


class Dog(Animal):
    def fetch(self, thing):
        print(self.name + 'goes after' + thing)

    def show_affection(self):
        print(self.name + ' puchhar hallaucha')


class Cat(Animal):
    def show_affection(self):
        print(self.name + ' meow meow garcha')

    def swat_string(self):
        print(self.name + ' khoi thaa bhayena')


class Snake(Dog):
    def show_affection(self):
        print('wow snakes do not show affection')


# Instantiation

python = Snake('python')

python.show_affection()

bhote_kukkur = Dog('Bhote Kukkor')

bhote_kukkur.eat('bhat')


for a in (Dog('bhuse'), Cat('kale'), Dog('gore'), Cat('Kale')):
    a.show_affection()


