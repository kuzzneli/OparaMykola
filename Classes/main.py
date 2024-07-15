
class Person:
    age = 0
    name = 'name'
    height = 10
    def __init__(self, age, name, height):
        self.age = age
        self.name = name
        self.height = height

    def grow(self):
        self.height += 5
