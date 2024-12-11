#Task No 83 " Implement a program that reads a CSV file and generates a bar chart to represent the data using Matplotlib"

#BAR Grapg

import matplotlib.pyplot as plt
from os import write
import pandas as pd

data = pd.read_csv('grades.csv')
fig,ax = plt.subplots()
ax.bar(data["Final"],data["Grade"])
ax.set_xlabel(data["Grade"])
ax.set_ylabel(data["Final"])
ax.set_title("Bar Graph")
plt.show()

#Pie Grapg
import matplotlib.pyplot as plt
from os import write
import pandas as pd

data = pd.read_csv('grades.csv')
fig,ax = plt.subplots()
sum1 = sum(data["Test1"])
sum2 = sum(data["Test2"])
sum3 = sum(data["Test3"])
sum4 = sum(data["Test4"])
student = [sum1,sum2,sum3,sum4]
color = ["blue", "orange", "red", "green"]
tests = ["Test1","Test2","Test3","Test4"]
exp = [0,0,0.1,0]
ax.pie(student , labels = tests , explode = exp , autopct = "%1.2f%%",colors = color)
plt.show()

# Bot Plot graph

import matplotlib.pyplot as plt
from os import write
import pandas as pd

data = pd.read_csv('grades.csv')
ax = data.boxplot(column = "Final", by = "Grade", figsize = (10,10))
ax.set_ylabel(data["Final"])
ax.set_title("Bot Pliot Braph")
plt.show()

# Plot Histogram

import matplotlib.pyplot as plt
from os import write
import pandas as pd

data = pd.read_csv('grades.csv')
grades_interval = [0, 250, 500, 750, 1000]
fig, ax = plt.subplots()
ax.hist(data["Final"], grades_interval)
ax.set_title("Histogram")
plt.show()

#Scatter Graph

import matplotlib.pyplot as plt
from os import write
import pandas as pd

data = pd.read_csv('grades.csv')
y = data["Final"]
x = data["Grade"]
z = data["Test1"]
plt.scatter(x,y,z)
plt.show()

# 3d graph

import matplotlib.pyplot as plt
from os import write
import numpy as np
import pandas as pd

data = pd.read_csv('grades.csv')
y = data["Final"]
x = data["Test1"]
z = data["Test2"]
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x, y, z, marker = "o", color = "green", mec = "red", mfc = "blue")
plt.show()

# Task No 84 "Write a function that reads a JSON file and extracts specific information from it)"

import matplotlib.pyplot as plt
from os import write
import numpy as np
import pandas as pd

data = pd.read_json('jdata.json', lines=True)
print(data)

# Task No 85 " Given a CSV file with temperature data for each day of the week, find the average temperature for each da"

import matplotlib.pyplot as plt
from os import write
import pandas as pd

data = pd.read_csv('weather.csv')
avg1 = sum(data["Data.Temperature.Max Temp"])/len(data["Data.Temperature.Max Temp"])
avg2 = sum(data["Data.Temperature.Min Temp"])/len(data["Data.Temperature.Min Temp"])
print("Average maximum Temperature: ", avg1)
print("Average minimum Temperature: ", avg2)

# Task No 86 "Create a class to represent a Student with attributes like name, age, and grades"

class student:
  def __init__(self, name,id, grade):
    self.name = name
    self.id = id
    self.grade = grade
student = student("Sami", 12, "A+")
print(student.name, student.id, student.grade)

# Task No 87  "Given a CSV file with employee details (name, position, salary), create a class to represent an Employee"

import pandas as pd

class employee:
  def __init__(self, name, position, salary):
    self.name = name
    self.position = position
    self.salary = salary
  def display(self):
    return self.name, self.position, self.salary
data = pd.read_csv('employees.csv')
employee = employee(data['FIRST_NAME'], data['JOB_ID'], data['SALARY'])
name, position, salary = employee.display()
print(name, " ", position, " ", salary)

# Task No 88 "Implement a program that simulates a basic bank account using a BankAccount class"

class BankAccount:
  name = ""
  age = 0
  account_type = ""
  balance = 0.0
  def __init__(self, name, age, account_type, balance):
    self.name = name
    self.age = age
    self.account_type = account_type
    self.balance = balance
  def display(self):
    print("Customer Name ",self.name)
    print("Customer  Age ",self.age)
    print("Customer  account type ",self.account_type)
    print("Customer  account balance ",self.balance)

name = input("Enter the name of customer ")
age = int(input("Enter the age of customer "))
account_type = input("Enter the account type ")
balance = float(input("Enter the total account Balance "))
obj = BankAccount(name, age, account_type, balance)
obj.display()

# Task No 89 "Write a Python program that uses a Rectangle class to calculate the area and perimeter of a rectangle7"
class rectangle:

  def __init__(self, width, length):
    self.width = width
    self.length = length

  def area(self):
    return self.width * self.length

  def display(self):
    print("Area of Rectangle: ", self.area())

def main():
  width = float(input("Enter the width of Rectangle: "))
  length = float(input("Enter the length of Rectangle: "))
  obj = rectangle(width, length)
  obj.display()

if __name__ == "__main__":
  main()

# class rectangle:

  def __init__(self, width, length):
    self.width = width
    self.length = length

  def area(self):
    return self.width * self.length

  def display(self):
    print("Area of Rectangle: ", self.area())

width = float(input("Enter the width of Rectangle: "))
length = float(input("Enter the length of Rectangle: "))
obj = rectangle(width, length)
obj.display()\


# Task No 90 "Create a class to represent a Car with attributes like make, model, and year"
class car:
  company = ""
  model = ""
  model_year = ""

  def __init__(self, company, model, model_year):
    company = company
    model = model
    model_year = model_year

  def display(self):
    print("Brand: ", company)
    print("Model: ", model)
    print("Model Year: ", model_year)


company = input("Enter the Car brand: ")
model = input("Enter the car model: ")
model_year = input("Enter the model year: ")
obj = car(company, model, model_year)
obj.display()

# Task No 91 " Given a JSON file with customer data, create a Customer class to store and manipulate the data7"

import json

data = []
name = input("Enter the name: ")
age  = input("Enter the age: ")
city = input("Enter the City: ")
data.append({"Name : ": name, "Age : ": age, "City : ": city})
f = open("data.json", "w")
json.dump(data, f, indent = 4)
f.close()
print("Data saved successfully")

# Using Append 

import json

with open('data.json', 'r') as file:
    existing_data = json.load(file)

name = input("Enter the name: ")
age  = input("Enter the age: ")
city = input("Enter the City: ")

new_data = {
    "name": name,
    "age": age,
    "city": city
}

existing_data.append(new_data)

with open('data.json', 'w') as file:
    json.dump(existing_data, file, indent=4)
print("Data saved successfully")

# Task No 92 "Write a program that uses a Person class to keep track of a person's name, age, and address7"
class person:
  name = ""
  age = 0
  address = ""
  def __init__(self, name, age, address):
    self.name = name
    self.age = age
    self.address = address
  def display(self):
    print(f"Name; {self.name}, Age: {self.age}, Address: {self.address}")

name = input("Enter the name: ")
age = input("Enter the age of person: ")
address = input("Enter the Address of peerson: ")
obj = person(name, age, address)
obj.display()