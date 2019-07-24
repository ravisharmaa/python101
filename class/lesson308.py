class InstanceCounter:

    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_value(self, newval):
        self.val = newval

    def get_value(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count


a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
    print("val of obj: %s" % (obj.get_value())) # the value of instance attribute eg 5, 13, 17
    print("count %s" % (obj.get_count())) # the vale of the class attribute which remains 3, why so? because the count is class attribute and it is set to 3 because we have 3 instance of it.




