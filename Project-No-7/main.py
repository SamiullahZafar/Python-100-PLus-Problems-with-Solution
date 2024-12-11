# Task NO 63 "Implement a function that takes two lists and returns their union (all unique elements from both lists)"

def unique(list1,list2):
  print("Unique Words in both lists: ")
  for i in list1:
    if i in list2:
      print(i)

list1 = ["apple", "banana", "orange", "kiwi", "strawberry"]
list2 = ["apple", "banana", "orange", "kiwi"]
print(unique(list1,list2))

# Task NO 64 "Given two dictionaries, merge them into a single dictionary"

dictionary = {}
dictionary1 = {}
dictionary2 = {}
key = input("Enter the key: ")
value = input("Enter the Value: ")
dictionary1[key] = value
key = input("Enter the key: ")
value = input("Enter the Value: ")
dictionary2[key] = value
dictionary1.update(dictionary2)
# dictionary = {**dictionary1,**dictionary2}
print("Dictionary is: ",dictionary)

# Task NO 65 "Write a program that finds the most frequent element in a list"
# Using Logic

def fre(list):
  count = 0
  temp = 0
  element = ""
  list2 = list
  list2 = set(list2)
  for i in list2:
    temp = 0
    for j in list:
      if i == j:
        temp += 1

    if count < temp:
      count = temp
      element = i

  return count,element

#using Dictionary

def fre(list):
  frequency = {}
  for i in list:
    if i in frequency:
      frequency[i] +=1
    else:
      frequency[i] = 1

  return frequency

list = [1, 2, 3, 1, 2, 1, 1, 3, 3, 3, 3, 3, 3]
count,Value = fre(list)
print("The most frequent element in the list is: ",fre(list))

# Task NO 66 "Implement a function that removes a key-value pair from a dictionary"

def remo(list,key):
  del list[key]
  return list

list = {'a': 1, 'b': 2, 'c': 3}
print("The most frequent element in the list is: ",remo(list,'c'))

# Task NO 67 "Create a program that checks if two sets have any elements in common"

def common(list1,list2):
  list1 = set(list1)

  list2 = set(list2)
  print("Same element: ")
  for i in list1:
    if i in list2: #we can use for loop also for j in list2: if i == j: print(i)
      print(i)

list1 = [1, 2, 3, 4, 5,7]
list2 = [4, 5, 6, 7, 8, 3]
common(list1,list2)

# Task NO 68 " Given a list of dictionaries, find the dictionary with the highest value for a specific key"

def list_dict():
  list_of_dicts = [
      {'name': 'John', 'age': 30},
      {'name': 'Alice', 'age': 25},
      {'name': 'Bob', 'age': 35}
  ]
  max_value = 0
  # for i in list_of_dicts:
  #   max_value.append(i['age'])
  print(max(max_value))
  return max_value

print(list_dict())

# Task NO 69 "Write a Python program that counts the number of occurrences of each character in a given string using a dictionary"

def accurance(list):
  count = {}
  for i in list:
    if i in count:
      count[i] += 1
    else:
      count[i] = 1
  print(count)

list = 'Hello world'
accurance(list)

# Task NO 70 "Given two sets, find the union, intersection, and difference between them"

def set_v(list1,list2):
  print("Union: ", list1.union(list2))
  print("Intersection: ", list1.intersection(list2))
  print("Difference: ", list1.difference(list2))

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set1 = {"apple", "banana", "orange", "kiwi"}
set2 = {"orange", "grape", "banana", "pineapple"}
set_v(set1,set2)

# Task NO 71 " Create a function that takes a list of dictionaries and sorts them based on a specified key"

my_dict = {'banana': 3, 'apple': 2, 'orange': 1}
sorted_dict_by_values = (sorted(my_dict.items(), key=lambda x: x[1]))
print(sorted_dict_by_values) 

sorted_dict = sorted(my_dict.items())
print(sorted_dict)

# Task NO 72 " Write a program that finds the average value of all the elements in a list of dictionarie"

def avera():
  my_dict = {'banana': 3, 'apple': 2, 'orange': 1}
  sum = 0
  lenth = len(my_dict)
  print(lenth)
  for i in my_dict:
    sum = sum + int(my_dict[i])
  print(sum/lenth)

avera()

#Short Method

my_dict = {'banana': 3, 'apple': 2, 'orange': 1}
sum_of = 0
sum_of = sum(my_dict.values())
print(sum_of/len(my_dict))
