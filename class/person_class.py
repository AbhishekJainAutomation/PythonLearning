class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} talk's a lot")

    def get_name(self):
        return self.name

person1 = Person('Abhishek Jain')
person1.talk()