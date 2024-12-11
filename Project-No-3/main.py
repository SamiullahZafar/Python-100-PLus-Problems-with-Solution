#Task No 22 "Implement a program that converts a given number of minutes into hours and minutes"
def time(minut):
  hours = minut//60
  seconds = minut*60
  return seconds,hours

minute = int(input("Please enter the time in minutes "))
seconds,hours = time(minute)
print("Time in seconds ",seconds)
print("Time in hours ",hours)

#Task No 23 " Create a function to count the number of vowels in a given strin"
def vowel(string):
  count = 0
  for i in string:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i=="O" or i == "U":
      count += 1
  return count

string = input("Enter the string ")
print("The number vowel in the string is ",vowel(string))

Task No 24 " Write a program to check if a number is prim"

def prime(num):
  return num % 2 == 0

num = int(input("Enter the number "))
if prime(num):
  print("The number is prime")
else:
  print("The number is not prime")

#Task No 25 "Write a program that checks if a given number is positive, negative, or zero."

def check(num):
  return num >= 0

num = int(input("Enter the number "))
if check(num):
  print("Tne entered number is either is positive or eqaul to zero")
else:
  print("The entered number is negative")

Task No 26 "Write a program that checks if a given number is positive, negative, or zero"

def check ():
  num = 0
  counter = 0
  while counter != 10:
    num += 1
    if num % 2 == 0:
      print(num)
      counter += 1

check()

#Task No 27 " Implement a program that finds the largest number in a list"

def large(num):
  temp = 0
  num = num.split()
  for i in  range(len(num)):
    num[i] = int(num[i])
    if num[i] > temp:
      temp = num[i]

  return temp

num = input("Enter the list ")

print("The largest Number in list is ",large(num))

num = input("Enter the list ")
num = num.split()
for i in range(len(num)):
  num[i] = int(num[i])
temp = max(num)
print("The largest Number in list is ",temp)

#Task No 28 " Create a program that takes a year as input and checks if it is a leap year or not/"
def is_leap_year(year):
  return year % 4 == 0

year = int(input("Enter a year: "))

if is_leap_year(year):
  print(year, "is a leap year.")
else:
  print(year, "is not a leap year.")

Task No 29 "Given a list of integers, find all the even numbers and store them in a new list"
def even(list):
  list1=[]
  list = list.split()
  for i in range(len(list)):
    list[i] = int(list[i])
    if list[i]%2==0:
      list1.append(list[i])
  return list1

list = input("Enter the list ")
print("Even number in list is ", even(list))

#Task No 30 "Given a list of integers, find all the even numbers and store them in a new list"
def prime(num):
  
  for i in range(2,num):
    if num % i == 0:
      temp = True
      break
    else:
      temp = False
  return temp


num = int(input("Enter the Number "))
if prime(num):
  print("Then number is not a prime number")
else:
  print("Then number is a prime number")

#Task No 31 "Create a program that generates the Fibonacci sequence up to a given number of terms"

def feb(num):
  num1 = 0
  num2 = 1
  nth = 0
  print("Fabonacci Searies ")
  print(num1)
  print(num2)
  count = 0
  while count != num:
    nth = num1 + num2
    num1 = num2
    num2 = nth
    print(nth)
    count +=1
    

num = int(input("Enter the number "))
feb(num)

#Task No 32 " Given a list of names, print all names starting with the letter 'A'"

def find(list):
  list = list.split()
  for i in list:
    if i[0]  == "a" or i[0]  == "A":
      print("Word is ",i)

list = input("Enter the list ")
find(list)

