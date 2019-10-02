# Abstract Classes Example
import abc


class GetterSetter:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_value(self, input):
        """Set a value in instance"""
        return

    @abc.abstractmethod
    def get_value(self):
        """Get and return a value from the instance..."""
        return


class MyClass(GetterSetter):

    def set_value(self, input):
        self.input = input

    def get_value(self):
        return self.input


my_class = MyClass()
my_class.set_value('yo value ho')
print(my_class.get_value())