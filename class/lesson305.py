# class MyClass:
#
#     def set_value(self, val):
#         self.value = val
#         return self
#
#     def get_value(self):
#         return self.value
#
#
# a = MyClass()
#
# print(a.set_value('10').get_value())
#
# a.value = 'hello'
#
# print(a.get_value())


class MyInteger:

    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val

    def get_val(self):
        return self.val

    def increment_val(self):
        self.val += 1


my_int = MyInteger()
my_int.set_val(10)

print(my_int.get_val())


my_int.set_val('hello')
print(my_int.get_val())
