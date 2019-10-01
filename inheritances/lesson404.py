import random


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('%s is eating %s' %(self.name, food))


class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['bhote','bhusya','local'])

    def fetch(self, thing):
        print('%s goes after the %s' % (self.name, thing))


bhote_kukkur = Dog('bhote_kukkur')
print(bhote_kukkur.name)
print(bhote_kukkur.breed)