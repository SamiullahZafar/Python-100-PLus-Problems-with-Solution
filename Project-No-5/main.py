#Task NO 43 "Create a function that takes a list of strings and returns the list sorted alphabetically"


def sorted_list(list):

  list = sorted(list)
  return list


list = ["banana", "apple", "cherry", "date"]
print("Sorted String ", sorted_list(list))

#Task NO 44 "Write a function that takes two lists and returns their intersection (common elements)"


def finder(list1, list2):
  print("Same elements in lists ")
  for i in list1:
    for j in list2:
      if i == j:
        print(i)


list1 = ['apple', 'banana', 'cherry', 'date']
list2 = ['apple', 'banana', 'cherry', 'Mango']
finder(list1, list2)

#Task NO 45 "Implement a function to check if a given year is a leap year or not "


def leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True  # Divisible by 400, so it's a leap year
      else:
        return False  # Divisible by 100 but not by 400, so it's not a leap year
    else:
      return True  # Divisible by 4 but not by 100, so it's a leap year
  else:
    return False  # Not divisible by 4, so it's not a leap year


year = int(input("Enter the year "))
if leap(year) == True:
  print("Leap Year")
else:
  print("Not Leap Year")

#Task NO 46 "Write a program that takes a sentence as input and counts the number of words in it"


def words(list):
  count = 0
  for i in list:
    if i == " ":
      count += 1

  return count + 1


list = input("Enter the List: ")
print("Number of words in the list ", words(list))

#Task NO 47 "Given a string, write a function to remove all vowels from it and return the modified string"


def rem(list):
  vowels = "aeioAEIOU"
  new_list = ""
  for i in list:
    if i not in vowels:
      new_list += i
  return new_list


list = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
print("List After remove vowels ", rem(list))

#Task NO 48 "Write a Python program to find the length of the longest word in a sentence"


def length(list):
  list = list.split()
  str = ""
  count = len(list[0])
  print(list[0])
  print(count)
  for i in list:
    if count < len(i):
      count = len(i)
      print(count)
      str = i
  return str


list = input("Entert the string please ")
print("Longest word in sentense", length(list))

#Task NO 49 "#Task NO 48 "Write a Python program to find the length of the longest word in a sentence"


def rev(list):
  list = list.split()
  str = ""
  print(list)
  for i in reversed(list):
    str += i + " "

  return str


list = input("Enter the String ")
print("Reversed String ", rev(list))

#Task NO 50 "Given a list of names, count the number of names that start with a vowel'"


def check(list):
  count = 0
  str = ""
  vowels = "aeiouAEIOU"
  for i in list:
    if i[0] in vowels:
      count += 1
      str += i + " "

  return count, str


list = [
    "Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Hannah",
    "Ivy", "Jack"
]
count, name = check(list)
print("Number of Names Start with vowels: ", count)
print("List of Names Start with vowels: ", name)

#Task NO 51 " Write a function to remove all duplicate characters from a given strin"


def dup(list):
  str = ""
  for i in list:
    if i not in str:
      str += i + "  "

  return str


list = [
    "Alice", "Bob", "Charlie", "David", "Emma", "Emma", "Frank", "Frank",
    "Grace", "Grace", "Hannah", "Ivy", "Jack"
]
print("list of Single words: ", dup(list))

#Task NO 52 " Implement a program that takes a sentence and a word as input and checks if the word is present in the sentenc"


def check(list, word):
  if word in list:
    return True
  else:
    return False


list = input("Enter the List: ")
word = input("Enter the word: ")
if check(list, word) == True:
  print("Word is prsenft in the Sentence")
else:
  print("Word is not present in the Sentence")
