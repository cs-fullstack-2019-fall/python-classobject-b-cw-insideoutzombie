### Problem 1:
# Create a class Dog. Make sure it has the attributes name, breed, color, gender.
# Create a function that will print all attributes of the class.
# Create an object of Dog in your problem1 function and print all of it's attributes.
class Dog:
    def __init__(self, name, breed, color, gender):
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender
    def printTheDog(self):
        print(f"{self.name}, {self.breed}, {self.color}, {self.gender}")

def problem1():
    dogBreed1 = Dog("Turbo", "PitBull", "Tan", "Male")
    dogBreed1.printTheDog()

### Problem 2:
##### We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with the equal sign.
# If the user doesn't enter the equal sign, ask them to input another string.
userInput = ""
while userInput != '=':
    userInput = input("Try again hit '=' ")

### Problem 3:
# Create a class Product that represents a product sold online. A product has a name, price, and quantity.
#
# The class should have several functions:
#
# a) One function that can change the name of the product.
#
# b) Another function that can change the name and price of the product.
#
# c) A last function that can change the name, price, and quantity of the product.
#
# Create an object of Product and print all of it's attributes.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def changeName(self, newName):
        self.name = newName

    def changeNamePrice(self, newName, newPrice):
        self.name = newName
        self.price = newPrice

    def changeNamePriceQuant(self, newName, newPrice, newQuantity):
        self.name = newName
        self.price = newPrice
        self.quantity = newQuantity


    def printProduct(self):
        print(f"{self.name}, {self.price}, {self.quantity}")

def problem2():
    newProduct = Product("iPad", "$300", "5")
    newProduct2 = Product("iPhone", "$450", "8")
    newProduct.printProduct()
    newProduct.changeName("David")
    newProduct.printProduct()
    newProduct2.changeNamePriceQuant("RaceCar", "$2000", "2")
    newProduct2.printProduct()

def main():
    # problem1()
    problem2()
main()
