### Animal is an object (look at the extra credit session)
class Animal(object):
    pass

## Dog is a class of animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has a name
        self.name = name

## Cat is a class of animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has a name
        self.name = name

## Person is an object
class Person(object):

    def __init__(self, name):
        ## Person has a name
        self.name = name

        ## Person has a pet of some kind
        self.pet = None

## Employee is a class of Person
class Employee(Person):

    def __init__(self, name, salary):
        ## reliably call init from base class
        ## python3 allows super() without declaring
        ## super(Employee, self)
        ## also may not be needed (see Fish())
        ## if you're not using multiple inheritance, where only the 
        ## first __init__ would be used

        ## more info : https://stackoverflow.com/questions/19608134/why-is-python-3-xs-super-magic
        super().__init__(name)
        ## Employees have a salary
        self.salary = salary

## Fish is an object
class Fish(object):
    ## Fish have colored scales
    def __init__(self, color):
        self.color = color

## Salmon is a class of Fish
class Salmon(Fish):
    pass

## Halibut is a class of Fish
class Halibut(Fish):
    pass

## rover is a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## mary is a Person
mary = Person("Mary")

## mary has a pet Cat
mary.pet = satan

## frank is an instance of Employee
frank = Employee("Frank", 120000)
print(f"Employee {frank.name} makes {frank.salary}")

## frank has a pet Dog
frank.pet = rover

## Flipper is a fish
flipper = Fish("blue")

## crouse is a Salmon
crouse = Salmon("pink")
print(f"This Salmon is {crouse.color}")

## Harry is a halibut
harry = Halibut("spotted")
