# using oop crete a class called cars that have the
# following attribute model,colour and year of manufacture
# implement constuctor method and a method function that prints
# ("my favorite car is _,it is this in colour_ and manufactured in this year" )
# create five instance of that class
from oop import myobj


class cars:
    def __init__(self, model, year,colour):
        self.model = model
        self.year = year
        self.colour = colour
def my_function(self):
    print(f"hello my new car is {self.model} of colour {self.colour} and year of manufacture {self.year}")
myobj=cars("Audi",2025,"blue")
my_function(myobj)
myobj2=cars("toyota", 2014,"white")
my_function(myobj2)
myobj3=cars("BMW",2024,"red")
my_function(myobj3)
myobj4=cars("Palo Alto",2025,"red")
my_function(myobj4)
myobj5=cars("Audi",2021,"blue")
my_function(myobj5)






