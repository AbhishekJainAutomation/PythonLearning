class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print('bark')


class Lovely:
    def lovely(self):
        print("lovely")


class Cat(Mammal, Lovely):
    # Python do not support emply class.
    # To help python interpretor we use pass to ask it to pass and skip the validation
    pass


dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.walk()
cat1.lovely()