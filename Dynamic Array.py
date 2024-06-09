class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = [None] * self.capacity
    
    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def _shift_left(self, index):
        for i in range(index, self.array):
            self.array[i] = self.array[i + 1]
        self.array[self.size] = None

    def append(self, element):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = element
        self.size += 1

    def get(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        raise IndexError("Index out of bounds")
        
    def remove(self, element):
        for i in range(self.size):
            if self.array[i] == element:
                self._shift_left(i)
                self.size -= 1
                if self.size == self.capacity // 4:
                    self._resize(self.capacity // 2)
                return
            raise ValueError("Element not found")
        
    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = element
        self.size += 1

# Example
arr = DynamicArray()
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
print(arr.array)