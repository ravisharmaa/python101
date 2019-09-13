class MaxSizeList:

    def __init__(self, length):
        self.length = length
        self.item_list = []

    def push(self, content):
        if len(self.item_list) >= self.length:
            return self.item_list

        return self.item_list.append(content)

    def get_list(self):
        return self.item_list


a = MaxSizeList(3)
a.push("Hello")
a.push("hi")
a.push("bi")
a.push("hu")

print(a.get_list())


b = MaxSizeList(1)
b.push("firstItem")
b.push("sec")

print(b.get_list())



