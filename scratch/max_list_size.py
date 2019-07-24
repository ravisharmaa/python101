class MaxListSize:

    def __init__(self, max_length):
        self.max_length = max_length
        self.container_list = []

    def push(self, item):
        if len(self.container_list) < self.max_length:
            self.container_list.append(item)
            return self

    def get_list(self):
        return self.container_list



