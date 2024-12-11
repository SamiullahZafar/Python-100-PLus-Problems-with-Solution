#Task No 53 "Given a list of numbers, find the sum and average using built-in functions."

def sum_avg(list):
  sum = 0
  avg = 0.0
  list = list.split()
  for i in list:
    i = int(i)
    sum = sum + i

  avg = sum / len(list)
  return avg

list = input("Enter the list of Number: ")
print("Average of list: ", sum_avg(list))

#Task No 54 "Create a list of fruits and add a new fruit to the list."

def find(fruit,list):
  list.append(fruit)
  return list

list = ["Apple", "Banana", "Orange"]
fruit = input("Enter the fruit name: ")
print("list of fruit: ",find(fruit,list))

Task No 55 "Access elements in a tuple using indexing"
def find(list):
  list = list.split()
  list = tuple(list)
  print(type(list))
  return list

list = input("Enter the List: ")
print("The List is: ",find(list))

#Task No 56 "Given two lists of numbers, concatenate them into a single list"

def concen(list1,list2):
  list1 = list1.split()
  list2 = list2.split()
  list1 = tuple(list1)
  list2 = tuple(list2)
  list3 = list1 + list2
  return list3

list1 = input("Enter the List 1: ")
list2 = input("Rnter the List 2: ")
print("Concentrated list is: ",concen(list1,list2))

#Task No 57 "Implement a function that takes a list of numbers and returns a new list with the squared values"

def square(list):
  sq = ""
  list = list.split()
  list = tuple(list)
  for i in list:
    i = int(i)
    i = i**2
    i = str(i)
    sq += i + " "
  return sq

list = input("Enter the List: ")
print(square(list))

#Task No 58 "Create a program that finds the common elements between two lists and stores them in a new list%"

def same_element(list1,list2):
  list1 = list1.split()
  list2 = list2.split()
  list3 = ""
  for i in list1:
    if i in list2:
      list3 += i + " "

  return list3

list1 = input("Enter the List: ")
list2 = input("Enter the List: ")
print("SAme element: ",same_element(list1,list2))

#Task No 59 "Write a Python program to count the occurrences of each element in a given list"

def element_counter(list):
  count = {}
  print(type(count))
  for i in list:
    if i in count:
      count[i] +=1
    else:
      count[i] = 1

  return count

list = ["apple", "banana", "apple", "orange", "banana", "apple", "kiwi", "strawberry", "kiwi", "apple"];
print(element_counter(list))

# Seacon Way 

list = ["apple", "banana", "apple", "orange", "banana", "apple", "kiwi", "strawberry", "kiwi", "apple"];
list2 = list
count = 0
list = set(list)
for i in list:
  count = 0
  for j in list2:
    if i == j:
      count +=1
  print(i ," : ",count)

#Task No 60 "#Task No 59 "Write a Python program to count the occurrences of each element in a given list"

def remove_duplicate(list):
  list2 = []
  for i in list:
    if i not in list2:
      list2.append(i)
    
  return list2

list = ["apple", "banana", "apple", "orange", "banana", "apple", "kiwi", "strawberry", "kiwi", "apple", "strawberry", "strawberry", "kiwi", "kiwi"]
print("Duplicate removed list: ",remove_duplicate(list))

#Task No 61 "Create a function that takes a list of strings and returns the list sorted by the length of the strings"

def sort_by_length(strings):
  
  sorted_strings = sorted(strings, key=len,reverse=True)
  return sorted_strings

list = ["apple", "banana", "applemmmmmmmmmmmm", "orange", "banana", "apple", "kiwi", "strawberry", "kiwi", "apple", "strawberry", "strawberry", "kiwi", "kiwi"]
print(sort_by_length(list))

#Task No 62 "Write a program that checks if a given list is sorted in ascending order"

def order(list):
  list1 = sorted(list)
  list2 = sorted(list,reverse=True)
  return list1,list2

list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
list1,list2=order(list)
print("Ascending Order: ",list1)
print("Descending Order: ",list2)