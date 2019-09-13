# class is an instance factory
# class defines an instance blueprint


class MyClass(object):

    var = 10

    # pass indicates that it has not content
    # it also indicates that the class has ended here

    pass


my_class_obj = MyClass()


print(my_class_obj)
# prints out <__main__.MyClass object at 0x7ff7fd8a8b00> which is unique and can be used later to determine the instance


print; print

print(my_class_obj.var)






