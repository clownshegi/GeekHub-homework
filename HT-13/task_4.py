"""
Create 'list'-like object, but index starts from 1 and index of 0 raises error.
Тобто це повинен бути клас, який буде поводити себе так, як list
(маючи основні методи), але індексація повинна починатись із 1
"""


class CustomList(list):
    def __init__(self, *args):
        super().__init__(args)

    def __getitem__(self, index):
        if index == 0:
            raise IndexError("Index starts from 1")
        elif index > 0:
            return super().__getitem__(index - 1)
        else:
            return super().__getitem__(index)

    def __setitem__(self, index, value):
        if index == 0:
            raise IndexError("Index starts from 1")
        elif index > 0:
            super().__setitem__(index - 1, value)
        else:
            super().__setitem__(index, value)

    def index(self, x, start=None, end=None):
        if start is not None:
            start -= 1
        if end is not None:
            end -= 1
        return super().index(x, start, end) + 1 if x in self[start:end] else -1

    def __str__(self):
        return super().__str__()[1:-1] if len(self) > 0 else '[]'


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

print(custom_list.count(15))  # 1

custom_list.sort()
print(custom_list)  # [10, 15, 20, 40, 50]

custom_list.reverse()
print(custom_list)  # [50, 40, 20, 15, 10]
