class MyNum:

    def __init__(self, val):
        try:
            value = int(val)
        except ValueError:
            value = 0

        self.val = value

    def increment(self):
        self.val = self.val + 100


my_num = MyNum()
my_num.increment()
my_num.increment()

print(my_num.val)
