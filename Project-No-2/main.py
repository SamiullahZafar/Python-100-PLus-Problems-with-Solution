# Task No 12 " Create a program that takes a sentence as input andcounts the number of words in it"

def given_string(str):
  count= 0
  for i in str:
    if i == " ":
      count += 1

  return count + 1

str = input("Enter the string ")
print("Number of words in string",given_string(str))

#Task NO 13 " Implement a program that swaps the values of two variable"

def swap(num1,num2):
  temp = num1
  num1 = num2
  num2 = temp

  return num1,num2

num1 = input("Please enter the first number")
num2 = input("Please enter the second number")
print("Before Swaing Number",num1,num2)
num1,num2=swap(num1,num2)
print("After Swaping Number",num1,num2)

#Task NO 14 "Given a list of numbers, find the sum and average"

def list_avg(list):
  sum = 0
  for i in list:
    i = int(i)
    sum=sum + i
  avg = sum/len(list)
  return avg

list = input("Enter list of Number")
list = list.split()
avg = list_avg(list)
print("Average of numbers ",avg)

#Task NO 15 "Create a program that takes a temperature in Celsius and converts it to Kelvin"

def kel(tem):
  tem = int(tem)
  kel = 0
  kel = tem + 273.15
  return kel

tem = input("Enter hte temperature in Celsius ")
print("Temperature in kelvin is ",kel(tem))

# Task NO 16 "Create variables for storing a person's name, age, and average test score"

name = input("Enter name of person ")
age = input("Enter age of person ")
score = input("Average test score ")

print("Name of a person ", name)
print("Age of person ", age)
print("Average of Person ", score)

#Task NO 17 "Concatenate two strings and print the result"

def concen(list1,list2):
  list3 = list1 + list2
  return list1,list2,list3

list1 = input("Enter the first list ")
list2 = input("Enter the secon list ")
list1,list2,list3 = concen(list1,list2)
print("The first list ",list1)
print("The secon list ",list2)
print("The Concentrated list ",list3)

# Task NO 18 "Create a list of fruits and access elements using indexing"

fruits = ["Apple","Banana","Orange","Pineapple","Mango"]
for i in fruits:
  print(i)

#Task NO 19 "Create a function to reverse a given string"

def rev(str):
  str = str.split()
  str.reverse()
  return str
    
str = input("Please the String ")
print("reversed string is ",rev(str))

def rev(str):
  str = str[::-1]
  str.reverse()
  return str

str = input("Please the String ")
print("reversed string is ",rev(str))

#Task NO 20 "Given a list of names, concatenate them into a single string separated by spaces"

def sp_sap(str1,str2):
  str = str1 +" "+str2
  return str

str1 = input("Enter the first String ")
str2 = input("Enter the second String ")
print("Composed String ",sp_sap(str1,str2))

#Task NO 20 "Write a Python program to check if a given string is apangram (contains all letters of the alphabet)'"

def pan(str):
  str = str.lower()
  temp = False
  str = list(str)
  for i in range(len(str)):
    if str[i] >= '0' and str[i] <= '9':
      temp = False
      break
    else:
      temp = True
  return temp
  
str = input("Please the string ")
if pan(str) == True:
  print("String is Panagram")
else:
  print("String is not Panagram")

#Task NO 21 "Calculate the area and circumference of a circle given its radius'"
import math

def circumference(r):
  circ = 2*math.pi*r
  return circ

def area(r):
  area = math.pi*r**2
  return area

radius = float(input("Enter the Radius of cirdle "))
print("Circumfarence of circle ",round(circumference(radius),2))
print("Area of circle ",round(area(radius),2))

