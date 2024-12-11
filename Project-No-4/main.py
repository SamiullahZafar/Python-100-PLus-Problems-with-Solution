#Tank No 33 "Implement a program that prints the multiplication table of a given number"

def table(num):
  for i in range(1,11):
    print(num, " x ",i," ",num*i)

num = int(input("Enter the number "))
table(num)

using while loop
def table(num):
   count = 0
   while count <= 10:
     print(num, " x ",count," ",num*count)
     count+=1

num = int(input("Enter the number "))
table(num)

#Tank No 34 "Write a program that calculates the factorial of a given number"

def fect(num):
  count = 1
  fac = 1
  while num >= count:
    fac = fac * count
    count += 1

  return fac

num = int(input("Enter the NUmber "))
print("Factorial of NUmber is ", fect(num))

USing built in function

import math

num = int(input("Enter the number "))
fact = math.factorial(num)
print("Factorial of number ",fact)

#Tank No 35 "Create a loop that prints all prime numbers between 1 and 50"

def pri(num):
  temp = True
  for i in range(2,num):
    for j in range(2,i):
      if i%j == 0:
        temp = False
        break
      else:
        temp = True
    if(temp):
      print("Prime Number ",i)

num = 50
num = int(num)
pri(num)

#Tank No 36 "Create a loop that prints all prime numbers between 1 and 50"
def number(list):
  count = 0
  for i in list:
    if len(i) > 5:
      count += 1
      print(i)
  print(count)

words_list = ["apple", "banana", "orange", "kiwi", "strawberry", "pineapple"]
number(words_list)


#Tank No 37 " Calculate the sum of digits of a given number"
def sum(num):
  temp = 0
  sum = 0
  while num > 0:
    temp = num % 10
    sum = sum + temp
    num = num // 10

  return sum
num = int(input("Enter the Number "))
print("Sum Breaked NUmber ",sum(num))

#Tank No 38 "Given a list of numbers, create a function to find the sum of all positive numbers"
def num(list):
  sum = 0
  list = list.split()
  for i in list:
    i = int(i)
    if i >= 0:
      sum  = sum + i

  return sum

list = input("Enter the LIst ")
print("Sum Positive number in list is ",num(list))

#Tank No 39 "Implement a function that returns the factorial of a given number using recursion"
def fact(num):
  if num > 0:
    return num * fact(num-1)
  else:
    return 1

num = int(input("Enter the NUmber "))
print("Factorial Of Number is ",fact(num))

#Tank No 40 "Create a function to find the square of each element in a given list"

def square(list):
  list =list.split()
  for i in list:
    i = int(i)
    print(i**2)

list = input("Enter the List ")
square(list)

#Tank No 41 "Write a function to check if a number is even or odd and return "Even" or "Odd" accordingly"

def check_unm(num):
  if num % 2 == 0:
    return "Even"
  else:
    return "Odd"

num = int(input("Enter the number "))
if check_unm(num)=="Even":
  print("Number is Even ")
else:
  print("Number is Odd ")

#Tank No 42 "Calculate the area of a triangle given its base and height using a function"
def tri_area(base,height):
  area = base * height/2
  return area

base = int(input("Enter the base ot triangle "))
height = int(input("Enter the hight ot triangle "))
print("Area Of triangle is ",tri_area(base,height))