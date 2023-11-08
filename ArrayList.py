class Array:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            return None

    def size(self):
        return len(self.data)

    def remove(self, value):
        if value in self.data:
            self.data.remove(value)

    def __str__(self):
        return str(self.data)

class ArrayList(Array):
    def insert(self, index, value):
        if 0 <= index <= len(self.data):
            self.data.insert(index, value)
        else:
            print("Index out of range")

    def pop(self, index=-1):
        if self.data:
            if 0 <= index < len(self.data):
                return self.data.pop(index)
            else:
                print("Index out of range")
        else:
            print("ArrayList is empty")