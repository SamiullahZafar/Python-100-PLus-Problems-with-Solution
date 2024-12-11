#Task No 1 "Print Hello World"
print("Hello World")

#Task No 2 "Calculate two numbers"
a = 10
b = 20
sum = a + b
print("Sum of NUmbers is =", sum)

#Task No 3 "Calculate Temperature F to C"
f = float(input("Enter Temperature in Fahrenheit ="))
c = (f - 32) * 5 / 9
print("Temperature in Celsius = ", c)

#from Fahrenheit to Celsius
c = float(input("Enter Temperature in Celsius ="))
f = (c * 9 / 5) + 32
print("Temperature in Fahrenheit = ", f)

#Task No 4 Calculate the area ot rectangle
l = float(input("Lenhth of Rectangle = "))
w = float(input("Width of Rectangle = "))
a = w * l
print("Area og Rectangle is = ", a)

#Task No 5 Print greeting message byu taking name and age as input
name = input("PLease the Name ")
age = int(input("Please Enter the age "))
print("AOA My name is ", name, "and my age is ", age)

#Task No 6 "Given Number is Even or odd"
number = int(input("Please the Number "))
if number % 2 == 0:
  print("Number is even ", number)
else:
  print("Number is odd ", number)

#Task No 7 "Max and min from list"
#using algorithem
num = input("Please Enter the Numbers separated by spaces: ")
num1 = num.split()

for i in range(len(num1)):
  num1[i] = int(num1[i])

max_num = num1[0]
min_num = num1[0]

for i in range(1, len(num1)):
  if num1[i] > max_num:
    max_num = num1[i]
  if num1[i] < min_num:
    min_num = num1[i]

print("Maximum Number is:", max_num)
print("Minimum Number is:", min_num)

#Short Method
num = input("Please Enter the Numbers separated by spaces: ")
num1 = num.split()
print("Maximum Number is:", max(num1))
print("Minimun Number is:", min(num1))

#Task No 8 "Chech string is palindrom or not"

my_str = "kayak"
my_str1 = ""
for i in my_str:
  my_str1 = i + my_str1
print(my_str1)

if my_str == my_str1:
  temp = True
else:
  temp = False

if temp == True:
  print("String is Palindrome")
else:
  print("String is not Palindrome")

#Task No 9 "Calculate the compound interest for a given principal amount interest rate time period"


def compoud_intrest(principle, rate, time, frequency):
  amount = principle * (1 + rate / frequency) + +(frequency / time)
  interest = amount - principle
  return interest


principle = float(input("Please enter your principle amount = "))
rate = float(input("Please enter the rate = "))
time = float(input("PLease enter the time period = "))
frequency = float(input("Please enter the frequen = "))
amount = compoud_intrest(principle, rate, time, frequency)
print("Your Compound intrest is ", amount)


#Task No 10 " Write a program that converts a given number of days into years, weeks, and days"
def days_weeks(days):
  year = int(days / 365)
  days = days - (year * 365)
  week = int(days / 7)
  days = days - (week * 7)

  return year, week, days


days = int(input("Please Enter the number od days "))
year, weeks, day = days_weeks(days)
print("Number of years ", year)
print("Number of weeks  ", weeks)
print("Number of days ", day)


#Task No 11 "  Given a list of integers, find the sum of all positive number"
def sum_positive(lists):

  sum = 0
  for i in range(len(lists)):
    lists[i] = int(lists[i])
    if (lists[i] > 0):
      sum = sum + lists[i]

  return sum


lists = input("Please Enter the list of numbers ")
lists = lists.split()
print("Sum of Positive numbers in the list ", sum_positive(lists))
