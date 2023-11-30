"""
Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.
"""
class MyClass:
    count_instances = 0

    def __new__(cls, *args, **kwargs):
        cls.count_instances += 1
        return super(MyClass, cls).__new__(cls)

    def __del__(self):
        type(self).count_instances -= 1

    @classmethod
    def get_instance_count(cls):
        return cls.count_instances



obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()
obj4 = MyClass()

print("Кількість екземплярів класу:", MyClass.get_instance_count())

del obj2

print("Кількість екземплярів класу після видалення одного екземпляра:", MyClass.get_instance_count())
