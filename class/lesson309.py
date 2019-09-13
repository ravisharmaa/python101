class MaxSizeList:

    def __init__(self, length):
        self.length = length
        self.itemList = []

    def push(self, content):
        if len(self.itemList) >= self.length:
            return self.itemList

        return self.itemList.append(content)

    def get_list(self):
        return self.itemList


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



