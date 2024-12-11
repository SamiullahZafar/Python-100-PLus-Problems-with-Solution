# Task No 93 " Implement a program that uses a Circle class to calculate the area and circumference of multiple circles"

import math
class circle:
  radius = 0.0
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    a = 0.0
    a = math.pi*(self.radius**2)
    return a

  def display(self):
    print(f"Area of Circumfarence is : {self.area()}")

i = 0
for i in range(3):
  radius = float(input("Enter the Radius of Circle: "))
  Circle = circle(radius)
  Circle.area()
  Circle.display()

# Task No 94 "Given a CSV file with product details (name, price, quantity), create a Product class to manage the data"

import pandas as pd

data = pd.read_csv("OnlineRetail.csv")
print(data)

Task No 95 " Create a class to represent a Movie with attributes like title, director, and rating"

class movie:
  title = ""
  director = ""
  rating = 0.0
  def __init__(self, title, director, rating):
    self.title = title
    self.director = director
    self.rating = rating
  def display(self):
    print(f"Movie title is {self.title} and Director Name is {self.director} and its rating is {self.rating}")

obj = movie("Avengers", "Rajkumar Hirani", 8.2)
obj.display()

# Task No 96 "Create a base class Animal with a method sound() and create derived classes Dog and Cat with their own sound()."

class dog:

  def sound(self):
    print("Dog Sounds Linke Baauuuu Baauuuu")

class cat:

  def sound(self):
    print("Cat Sounds Like Miaaauunnn Miaaauunnn")

obj1 = dog()
obj1.sound()
obj2 = cat()
obj2.sound()

# Task No 97 "Implement a class hierarchy to represent different types of vehicles (Car, Bike) with their own attributes and  methods."

class car:
  type = ""
  model = 0.0
  company = ""
  def __init__(self, type, model, company):
    self.type = type
    self.model = model
    self.company = company
  def display(self):
    print(f"Type is {self.type} and Model is {self.model} and Company is {self.company}")

class bike:
  type = ""
  model = 0.0
  company = ""
  def __init__(self, type, model, company):
    self.type = type
    self.model = model
    self.company = company
  def display(self):
    print(f"Type is {self.type} and Model is {self.model} and Company is {self.company}")

type = input("Enter the type of vehicle: ")
model = int(input("Enter the model of vehicle: "))
company = input("Enter the company of vehicle: ")
obj1 = car(type, model, company)
obj1.display()
type = input("Enter the type of vehicle: ")
model = int(input("Enter the model of vehicle: "))
company = input("Enter the company of vehicle: ")
obj2 = bike(type, model, company)
obj2.display()

# Task No 97 " Create a class Person with private attributes and define methods to get and set the values of those attributes"

class Person:
  def __init__(self, name, age, address):
      self.name = name
      self.age = age
      self.address = address

  def get_name(self):
      return self.name

  def get_age(self):
      return self.age

  def get_address(self):
      return self.address

  def set_name(self, name):
      self.name = name

  def set_age(self, age):
      self.age = age

  def set_address(self, address):
      self.address = address

# Example usage
person1 = Person("John", 30, "123 Main Street")
print(person1.get_name())  # Output: John
print(person1.get_age())   # Output: 30
print(person1.get_address())  # Output: 123 Main Street

person1.set_name("Alice")
person1.set_age(25)
person1.set_address("456 Elm Street")

print(person1.get_name())  # Output: Alice
print(person1.get_age())   # Output: 25
print(person1.get_address())  # Output: 456 Elm Street

# Task No 98 "Create a base class Shape with methods to calculate area and perimeter, and derive classes Circle and Square3"

import math

class shapes:

  def area(self):
    pass

  def perimeter(self):
    pass

class Circle(shapes):

  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return math.pi * (self.radius**2)

  def perimeter(self):
    return (2 * math.pi * self.radius)

class Square(shapes):

  def __init__(self, side):
    self.side = side

  def area(self):
    return self.side**2

  def perimeter(self):
    return 4 * self.side

r = float(input("Enter the radius of circle: "))
s = float(input("Enter the side of square: "))
obj1 = Circle(r)
obj2 = Square(s)
print(f"Area of Circle is {obj1.area()} and perimeter of Circle is {obj1.perimeter()}")
print(f"Area of Square is {obj2.area()} and perimeter of Square is {obj2.perimeter()}")

# Task No 99 "Implement a class hierarchy to represent different types of employees (Manager, Engineer) with their attributes3"

class Employee:
  def __init__(self, name, age, salary):
      self.name = name
      self.age = age
      self.salary = salary

  def display_info(self):
      print(f"Name: {self.name}, Age: {self.age}, Salary: ${self.salary}")

class Manager(Employee):
  def __init__(self, name, age, salary, department):
      super().__init__(name, age, salary)
      self.department = department

  def display_info(self):
      super().display_info()
      print(f"Department: {self.department}")

class Engineer(Employee):
  def __init__(self, name, age, salary, specialization):
      super().__init__(name, age, salary)
      self.specialization = specialization

  def display_info(self):
      super().display_info()
      print(f"Specialization: {self.specialization}")

# Example usage
manager = Manager("John Doe", 40, 80000, "Engineering")
engineer = Engineer("Jane Smith", 30, 60000, "Software Development")

manager.display_info()
engineer.display_info()

# Task No 100 "Write a Python program that uses inheritance to represent a hierarchy of shapes (Triangle, Rectangle, etc.)"

class shape:
  def triangle(self):
    pass
  def rectangle(self):
    pass

class Triangle(shape):
  def __init__(self,  base, height):
    self.base = base
    self.height = height

  def triangle(self):
    return (self.base*self.height)/2

class Rectangle(shape):
  def __init__(self,  length, width):
    self.length = length
    self.width = width

  def rectangle(self):
    return self.length*self.width

obj1 = Triangle(10, 20)
obj2 = Rectangle(10, 20)
print(f"Area of Triangle is {obj1.triangle()}")
print(f"Area of Rectangle is {obj2.rectangle()}")

# Task No 101  "Create a class hierarchy to represent different types of animals (Bird, Fish) with their own attributes and methods3"

class animal:

  def bird(self, name):
    pass

  def fish(self, name):
    pass

class Bird(animal):

  def __init__(self, name):
    self.name = name

  def bird(self):
    print(f"{self.name} is flying")

class Fish(animal):

  def __init__(self, name):
    self.name = name

  def fish(self):
    print(f"{self.name} is Swimming")

obj1 = Bird("Eagle")
obj2 = Fish("Dambra")
obj1.bird()
obj2.fish()

# Task No 102 "Given a JSON file with product details (name, price, quantity), create a Product class with encapsulated attributes3"

import json
import os

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_data(self):
        if os.path.exists('product.json') and os.path.getsize('product.json') > 0:
            with open('product.json', 'r') as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        new_data = {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }
        existing_data.append(new_data)

        with open('product.json', 'w') as file:
            json.dump(existing_data, file, indent=4)

    def display(self):
        with open('product.json', 'r') as file:
            json_data = json.load(file)
        print(json_data)


name = input("Enter the name of product: ")
price = float(input("Enter the price of product: "))
quantity = int(input("Enter the quantity of product: "))
obj1 = Product(name, price, quantity)
obj1.add_data()
obj1.display()

