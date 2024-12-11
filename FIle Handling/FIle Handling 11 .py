#Task No 103 "Implement a program that uses inheritance to represent a hierarchy of vehicles (Car, Bike, Truck, etc.)"
class Vehicle:

  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def display_info(self):
    print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


class Car(Vehicle):

  def __init__(self, make, model, year, num_doors):
    super().__init__(make, model, year)
    self.num_doors = num_doors

  def display_info(self):
    super().display_info()
    print(f"Number of doors: {self.num_doors}")


class Bike(Vehicle):

  def __init__(self, make, model, year, num_gears):
    super().__init__(make, model, year)
    self.num_gears = num_gears

  def display_info(self):
    super().display_info()
    print(f"Number of gears: {self.num_gears}")


class Truck(Vehicle):

  def __init__(self, make, model, year, payload_capacity):
    super().__init__(make, model, year)
    self.payload_capacity = payload_capacity

  def display_info(self):
    super().display_info()
    print(f"Payload capacity: {self.payload_capacity} tons")


# Example usage
car = Car("Toyota", "Camry", 2022, 4)
car.display_info()

print()

bike = Bike("Giant", "Anthem", 2020, 21)
bike.display_info()

print()

truck = Truck("Ford", "F-150", 2023, 2.5)
truck.display_info()

#Task No 104 "Write a Python program that uses encapsulation to protect sensitive information in a User class."


class Vehicle:

  def __init__(self, make, model):
    self._make = make  # protected attribute
    self._model = model  # protected attribute

  def display_info(self):
    print(f"Make: {self._make}, Model: {self._model}")


class Car(Vehicle):

  def __init__(self, make, model, year):
    super().__init__(make, model)
    self.year = year

  def display_info(self):
    super().display_info()
    print(f"Year: {self.year}")


# Vehicle = Vehicle("Toyota", "Camry", 2022)
# Vehicle.display_info()
car = Car("Toyota", "Camry", 2022)

# Accessing protected attributes directly (not recommended, but possible)
print(car._make)  # Output: Toyota
print(car._model)  # Output: Camry
car.display_info()

#Task No 105 "Create a class hierarchy to represent different types of electronics (Phone, Laptop) with their attributes"


class phone:

  def __init__(self, name, model, company):
    self.name = name
    self.model = model
    self.company = company

  def display(self):
    print("Phone Details")
    print(
        f"Name: {self.name}, Model: {self.model}, Company: {self.company} \n")


class laptop:

  def __init__(self, name, model, company, year):
    self.name = name
    self.model = model
    self.company = company
    self.year = year

  def display(self):
    print("Laptop Details")
    print(
        f"Name: {self.name} \nModel: {self.model} \nCompany: {self.company} \nYear: {self.year}"
    )


phone_instance = phone("iPhone", "14", "Apple")
phone_instance.display()
laptop_instance = laptop("macbook", "OMEN", "HP", 2022)
laptop_instance.display()

#Task No 106 "Given a CSV file with employee details (name, position, salary), create an Employee class with private attributes$"

import pandas as pd


class employee:

  def __init__(self, fname, lname, position, salary):
    self.__fname = fname
    self.__lname = lname
    self.__position = position
    self.__salary = salary

  def dispaly_info(self):
    print(
        f"First Name: {self.__fname} Last Name: {self.__lname} Position: {self.__position} Salary: {self.__salary}"
    )

data = pd.read_csv("employees.csv")
emp = employee(data["FIRST_NAME"], data["LAST_NAME"], data["JOB_ID"],
               data["SALARY"])
emp.dispaly_info()

#Task No 107 "Implement a program that uses inheritance to represent a hierarchy of shapes (Circle, Triangle, Rectangle, etc.)."

import math


class Shape:

  def __init__(self):
    pass

  def area(self):
    pass

  def perimeter(self):
    pass


class Circle(Shape):

  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return math.pi * self.radius**2

  def perimeter(self):
    return 2 * math.pi * self.radius


class Triangle(Shape):

  def __init__(self, side1, side2, side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3

  def area(self):
    s = (self.side1 + self.side2 + self.side3) / 2
    return math.sqrt(s * (s - self.side1) * (s - self.side2) *
                     (s - self.side3))

  def perimeter(self):
    return self.side1 + self.side2 + self.side3


class Rectangle(Shape):

  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width

  def perimeter(self):
    return 2 * (self.length + self.width)


r = int(input("Enter the radius of the circle: "))
obj1 = Circle(r)
print("Area of Circle:", obj1.area())
print("Perimeter of Circle:", obj1.perimeter())

side1 = int(input("Enter the Side 1 of triangle: "))
side2 = int(input("Enter the Side 2 of triangle: "))
side3 = int(input("Enter the Side 3 of triangle: "))
obj2 = Triangle(side1, side2, side3)
print("Area of Triangle:", obj2.area())
print("Perimeter of Triangle:", obj2.perimeter())

length = int(input("Enter the Length of Rectangle: "))
width = int(input("Enter the width of Rectangle: "))

obj3 = Rectangle(length, width)
print("Area of Rectangle:", obj3.area())
print("Perimeter of Rectangle:", obj3.perimeter())
