import abc


class GetSetParent:
    __metaclass__ = abc.ABCMeta

    def __init__(self, value):
        self.value = 0

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    @abc.abstractmethod
    def show_doc(self):
        return


class GetSetInt(GetSetParent):

    def set_value(self, value):
        if not isinstance(value, int):
            value = 0
        super(GetSetInt, self).set_value(value)

    def show_doc(self):
        print('GetsetInt object {0}, only accepts integer values'. format(id(self)))


class GetSetList(GetSetParent):
    def __init__(self, value):
        self.value_list = [value]

    def get_value(self):
        return self.value_list[-1]

    def get_values(self):
        return self.value_list

    def set_value(self, value):
        self.value_list.append(value)

    def show_doc(self):
        print('GetSetList object, len {0}, stores history of values set'. format(len(self.value_list)))


x = GetSetInt(3)
x.set_value(5)
print(x.get_value())
x.show_doc()


gsl = GetSetList(5)
gsl.set_value(10)
gsl.set_value(20)

print(gsl.get_value())

print(gsl.get_values())

gsl.show_doc()



