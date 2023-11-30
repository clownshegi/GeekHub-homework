"""
Create 'list'-like object, but index starts from 1 and index of 0 raises error.
Тобто це повинен бути клас, який буде поводити себе так, як list
(маючи основні методи), але індексація повинна починатись із 1
"""
class CustomList:
    def __init__(self, *args):
        self._data = list(args)

    def append(self, x):
        self._data.append(x)

    def extend(self, iterable):
        self._data.extend(iterable)

    def insert(self, i, x):
        if i < 1:
            raise IndexError("Index starts from 1")
        self._data.insert(i - 1, x)

    def remove(self, x):
        self._data.remove(x)

    def pop(self, i=None):
        if i is None:
            return self._data.pop()
        return self._data.pop(i)

    def index(self, x, start=None, end=None):
        if start is None:
            start = 1
        else:
            start = max(1, start)
        if end is None:
            end = len(self._data)
        else:
            end = max(1, end)
        return self._data.index(x, start - 1, end) + 1

    def count(self, x):
        return self._data.count(x)

    def sort(self):
        self._data.sort()

    def reverse(self):
        self._data.reverse()

    def clear(self):
        self._data.clear()

    def copy(self):
        return self._data.copy()

    def __getitem__(self, index):
        if index < 1:
            raise IndexError("Index starts from 1")
        return self._data[index - 1]

    def __setitem__(self, index, value):
        if index < 1:
            raise IndexError("Index starts from 1")
        self._data[index - 1] = value

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)


custom_list = CustomList(10, 20, 30)
print(custom_list)  # [10, 20, 30]

custom_list.append(40)
print(custom_list)  # [10, 20, 30, 40]

custom_list.extend([50, 60])
print(custom_list)  # [10, 20, 30, 40, 50, 60]

custom_list.insert(2, 15)
print(custom_list)  # [10, 15, 20, 30, 40, 50, 60]

custom_list.remove(30)
print(custom_list)  # [10, 15, 20, 40, 50, 60]

print(custom_list.pop())  # 60
print(custom_list)  # [10, 15, 20, 40, 50]

print(custom_list.index(20))  # 3

print(custom_list.count(15))  # 2

custom_list.sort()
print(custom_list)  # [10, 15, 20, 40, 50]

custom_list.reverse()
print(custom_list)  # [50, 40, 20, 15, 10]

custom_list.clear()
print(custom_list)  # []
