import random


class MyClass(object):

    # notice that the rand_val is not in the class
    # but in the instance

    def do_this(self):
        self.rand_val = random.randint(1, 10)


my_class = MyClass()
my_class.do_this()
print(my_class.rand_val)
