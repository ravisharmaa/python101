class InstanceCounter:
    count = 0

    def __init__(self, value):
        self.value = value
        InstanceCounter.count += 1

    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value

    @classmethod
    def get_count(cls):
        return cls.count


a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
    print('val of obj %s' %(obj.get_value()))
    print("count of %s" %(obj.get_count()))

print(InstanceCounter.get_count())
print("----------------------------------")

# static method example


class AnotherInstanceCounter:
    count = 0

    def __init__(self, value):
        self.value = self.filter_int(value)
        AnotherInstanceCounter.count += 1

    def get_value(self):
        return self.value

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def filter_int(value):
        if not isinstance(value, int):
            return 0

        return value


d = AnotherInstanceCounter(8)
e = AnotherInstanceCounter(9)
f = AnotherInstanceCounter('hello')

for abc in (d, e, f):
    print('count of count %s' % (abc.get_count()))
    print('value of object %s' % (abc.get_value()))
    print("-----")


