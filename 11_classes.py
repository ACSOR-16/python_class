### classes

# definition

class MyEmptyPerson:
    pass # empty

print(MyEmptyPerson)
print(MyEmptyPerson())

print(" --- " * 10)
# class with constructor, functions and props private and public

class Person:
    def __init__(self, name, surname, nickname = "Has no nickname"):
        self.full_name = f"{name} {surname} and {nickname}" #prop public
        self._name = name # private prop

    def get_name(self):
        return self._name
    
    def walk(self):
        print(f"{self.full_name} is walking")

my_person = Person("oscar", "aguirre")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

print(" --- " * 10)

my_other_person = Person("will", "tara", "cso")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector leon (crazy dogs)"
print(my_other_person.full_name)

print(" --- " * 10)

my_other_person.full_name = 788
print(my_other_person.full_name)
print(my_other_person._name)