# class attributes and instance attributes


class YourClass(object):

    # class variable
    classy = 10

    def set_val(self):
        # instance variable

        self.insty = 100


dd = YourClass()

print(dd.classy)

dd.classy = 'some another val'

print(dd.classy)

del dd.classy

print(dd.classy)

dd.set_val()

print(dd.insty)
print(dd.classy)

