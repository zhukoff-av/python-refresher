class Person:
    def __init__(self, name):
        self.name = name

    def print_obj(self):
        print(self.name)


class SpecificPerson(Person):
    def print_obj(self):
        print(f"Specific Person {self.name}")


yo = Person('Yo')
spec = SpecificPerson('Spec')

yo.print_obj()
spec.print_obj()
