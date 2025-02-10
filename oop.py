# object oriented programing
class Person:
    def __init__(self, name, age):
        # this is constructor method?
        # it take two parameters and intialize as attribute
        self.name = name
        self.age = age
    def my_function(self):
        print(f"hello my name is {self.name} and my age is {self.age}")
        # this is a method function
# create an objector an instanceof a class
myobj = Person("John", 18)
myobj.my_function()
myobj2=person = Person("jame", 14)
myobj2.my_function()



